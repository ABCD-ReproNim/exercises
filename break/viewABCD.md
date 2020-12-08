---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import os
from pathlib import Path
from glob import glob
from collections import namedtuple

import requests
```

### Gather all the data elements from all the txt files

The ABCD3 folder contains a number of tab-delimited text files with ABCD data.
We will collect all of these files and then load them into pandas DataFrames
to compile and access the data.

```python
data_path = Path("/home/jovyan/ABCD3")
files = sorted(data_path.glob("*.txt"))
```

```python
# We store the info in 4 different Python datatypes
data_elements = []
data_structures = {}
event_names = set()
StructureInfo = namedtuple("StructureInfo", field_names=["description", "eventnames"])

for fl in files:
    # Extract data structure from filename
    data_structure = Path(fl).name.split('.txt')[0]
    
    # Read the data structure and capture all the elements from the file
    # Note this could have been done using the data returned from the NDA API
    # We are using pandas to read both the first and second rows of the file as the header
    df = pd.read_table(fl, header=[0, 1], nrows=0)
    for val in df.columns.values.tolist():
        val = list(val)
        val.append(data_structure)
        data_elements.append(val)
    
    # (Optional) Retrieve the eventnames in each structure. Some structures were only collected
    # at baseline while others were collected at specific or multiple timepoints
    events_in_structure = None
    if any(['eventname' == val[0] for val in df.columns]):
        # Here we are skipping the 2nd row of the file containing desciption using skiprows
        df = pd.read_table(fl, skiprows=[1], usecols=['eventname'])
        events_in_structure = df.eventname.unique().tolist()
        event_names.update(events_in_structure)

    # (Optional) Retrieve the title for the structure using the NDA API
    rinfo = requests.get(f"https://nda.nih.gov/api/datadictionary/datastructure/{data_structure}").json()
    data_structures[data_structure] = StructureInfo(description=rinfo["title"] if "title" in rinfo else None,
                                                    eventnames=events_in_structure)

# Convert to a Pandas dataframe
data_elements = pd.DataFrame(data_elements, columns=["element", "description", "structure"])
```

```python
data_elements.head()
```

```python
data_elements.shape
```

```python
len(data_structures)
```

```python
event_names
```

#### Find all structures that have baseline data

```python
NOEVENTS = {}
for key, val in data_structures.items():
    if val.eventnames:
        if 'baseline_year_1_arm_1' in val.eventnames:
            print(f"{key}: {val.description}")
    else:
        NOEVENTS[key] = val
```

Structures with no eventname

```python
for key, val in NOEVENTS.items():
    print(f"{key}: {val.description}")
```

#### Save data elements to a tab-separated file

```python
data_elements.to_csv("data_elements.tsv", sep="\t", index=None)
```

#### Number of unique data elements

```python
data_elements.element.unique().shape
```

```python
data_elements[data_elements.element == "smri_vol_scs_amygdalalh"]
```

#### Use the following code block to quickly introspect variables in a structure

```python
structure = 'abcd_mri01' #'abcd_psb01'
df = pd.read_table(f"/home/jovyan/ABCD3/{structure}.txt", header=[0, 1], nrows=0)
df.columns.tolist()
```

```python
common = ["subjectkey", "interview_date", "interview_age", "eventname", "sex"]
demographic = ["site_id_l", "anthroheightcalc", "anthroweightcalc", "ehi_y_ss_scoreb", 'neighborhood_crime_y', 'snellen_aid_y']
clinical = ['ksads_1_2_t', 'ksads_8_29_t', 'ksads_25_33_t', 'ksads_13_929_t', 'pps_y_ss_severity_score']
behavioral = ['prosocial_q2_y', 'prosocial_q3_y'] # 'fit_ss_sleepperiod_minutes', 'fit_ss_avg_hr_deep',
cognitive = []
imaging = ["smri_vol_cdk_total", "smri_vol_scs_amygdalalh", 'mri_info_manufacturer',]

all_variables = demographic + clinical + behavioral + cognitive + imaging
```

#### Find the data structures that contain the elements

```python
structures2read = {}
for element in all_variables:
    item = data_elements[data_elements.element == element].structure.values[0]
    if item not in structures2read:
        structures2read[item] = []
    structures2read[item].append(element)
structures2read
```

#### Construct a new table of data containing the variables

```python
# Read data from one structure
df = pd.read_table(Path("/home/jovyan/ABCD3/") / (list(structures2read)[0] + ".txt"), skiprows=[1], low_memory=False,
                  usecols=common + structures2read[list(structures2read)[0]])
df.head()
```

```python
all_df = None
count = 0
for structure, elements in structures2read.items():
    df = pd.read_table(Path("/home/jovyan/ABCD3/") / (structure + ".txt"), skiprows=[1], low_memory=False, usecols=common + elements)
    df = df[df.eventname == 'baseline_year_1_arm_1']
    if all_df is None:
        all_df = df[["subjectkey", "interview_date", "interview_age", "sex"] + elements]
    else:
        all_df = all_df.merge(df[['subjectkey'] + elements], how='outer')
        pass #all_df = all_df.merge(df[['subjectkey'] + elements], left_on='subjectkey', right_on='subjectkey')
    count += 1
    if count == 3:
        ...
```

```python
all_df.head()
```

```python
all_df.shape, all_df.subjectkey.unique().shape
```

#### Choose a random subset of participants

Every time your run the following code, a random set of 1000 participants is chosen. How would you alter this code to choose the same N participants each time?

```python
N = 1000
indices = np.random.randint(0, high=all_df.shape[0] + 1, size=N)
new_df = all_df.loc[indices, :]
new_df.shape
```

```python
new_df.describe()
```

### Display a linear regression between two variables for two groups

```python
# Make a custom palette with gendered colors
pal = dict(M="#6495ED", F="#F08080")

# Show the survival probability as a function of age and sex
g = sns.lmplot(x='pps_y_ss_severity_score', y='smri_vol_cdk_total', col="sex", hue="sex", data=new_df,
               palette=pal, y_jitter=.02, logistic=False, truncate=False)
```

### Display relations between 4 variables color coded by a categorical variable

```python
sns.pairplot(new_df, hue="sex", vars=["anthroweightcalc", 'ksads_1_2_t', 'prosocial_q2_y', "smri_vol_scs_amygdalalh"]);
```

### Create an interactive plot that allows viewing many variables

```python
# Create an interactive parallel coordinate plot
new_df_numerical = new_df.copy()
new_df_numerical.sex = new_df.sex.astype("category").cat.codes
new_df_numerical.site_id_l = new_df.site_id_l.astype("category").cat.codes
fig = px.parallel_coordinates(new_df_numerical, color="interview_age", 
                              dimensions=["interview_age", "sex"] + all_variables,
                              color_continuous_scale=px.colors.sequential.Agsunset,)
                              #color_continuous_midpoint=2)
fig.show()
```

### Display effects of two categories on a continuous variable

```python
plt.figure(figsize=(15, 6))
sns.violinplot(data=new_df, x="mri_info_manufacturer", y="smri_vol_cdk_total", hue="sex",
               split=True, inner="quart", linewidth=1,
               palette={"M": "#FF9914", "F": ".85"})
sns.despine(left=True)
```

```python

```
