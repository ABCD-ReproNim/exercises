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

# Select and Visualize ABCD Data
This notebook walks you through reading, filtering, and
visualizing ABCD data you downloaded in the previous step.
After this notebook is run you should be able to:
1. read data from a file into python
2. select data using control flow methods
3. visualize data

## Non-exhaustive list of concepts used in this notebook
You do not need a solid grasp of all these concepts to benefit
from running through this notebook, but we have provided a non-exhaustive
list of concepts used in this notebook.
Each concept has a relevant article linked and an example of how that concept
is used in the notebook.

- python/programming language concepts
    - [libraries/importing](https://realpython.com/python-modules-packages/)
        - `import numpy as np`
    - [variables](https://realpython.com/python-variables/)
        - `data_elements = []`
    - [functions](https://realpython.com/defining-your-own-python-function/#functions-in-python)
        - `len(data_structures)`
- data structures
    - [lists](https://realpython.com/python-lists-tuples/)
        - `["subjectkey", "interview_date", "interview_age", "eventname", "sex"]`
    - [sets](https://realpython.com/python-sets/)
        - `{'18_month_follow_up_arm_1', 'baseline_year_1_arm_1', ..., 'screener_arm_1'}`
    - [pandas dataframes](https://realpython.com/pandas-dataframe/)
        - `pd.DataFrame(data_elements, columns=["element", "description", "structure"])`
- control structures
    - [if statements](https://realpython.com/python-conditional-statements/)
        - `if any(['eventname' == data_element for data_element in data_structure_df.columns.levels[0]]):
                ...`
    - [for loops](https://realpython.com/python-for-loop/)
        - `for data_structure, info in data_structures.items():
                ...`
- unix concepts
    - [globbing](https://swcarpentry.github.io/python-novice-inflammation/06-files/index.html)
        - `sorted(data_path.glob("*.txt"))`
    - [folders/directories](http://swcarpentry.github.io/shell-novice/02-filedir/index.html),
      [connection to python through pathlib](https://realpython.com/python-pathlib/)
        - `data_path = Path("/home/jovyan/ABCD3")`

- misc
    - [f-strings](https://realpython.com/python-f-strings/)
        - `f"/home/jovyan/ABCD3/{structure}.txt"`

### Import all libraries
By convention all libraries being used are read in at the top of a notebook/script.
```python
import pandas as pd # to read/manipulate/write data from files
import numpy as np # to manipulate data/generate random numbers
import plotly.express as px # interactive visualizations
import seaborn as sns # static visualizations
import matplotlib.pyplot as plt # fine tune control over visualizations

from pathlib import Path # represent and interact with directories/folders in the operating system
from collections import namedtuple # structure data in an easy to consume way

import requests # retrieve data from an online source
```

### Gather all the data elements from all the txt files

The ABCD3 folder contains a number of tab-delimited text files with ABCD data.
We will first collect all of these files and then load them into pandas DataFrames
to compile and access the data.

Below we collect the files into a variable with the name `files`
```python
# save directory we downloaded the ABCD data to `data_path`
data_path = Path("/home/jovyan/ABCD3")
# glob (match) all text files in the `data_path` directory
files = sorted(data_path.glob("*.txt"))
```

After collecting the files, we need to extract information about
the data structures and the data elements.
The data structures are the text file names (e.g., `abcd_abcls01`)
which indicate the type of data stored inside the text file.
The data elements are the column names inside the tab delimited
text file.
The data structure and data element names are condensed to make working
with them programmatically easier, but it is difficult for a human
to interpret what `abcd_abcls01` means.
So in addition to aggregating data structure and data element names
together, we are also collecting their metadata to have a human readable description
of their condensed names.
The data element metadata is located in the data structure files themselves
as the second row of the file, however, the data structure metadata was not downloaded
necessitating a query to the NDA website to retrieve the human readable
description of the data structure (using `requests`).

Finally, since we are only interested in the baseline measures, we need to keep track of
what names are given to each event in each of the data structures.
```python
# We store the info in 4 different Python datatypes
data_elements = []
data_structures = {}
event_names = set()
StructureInfo = namedtuple("StructureInfo", field_names=["description", "eventnames"])

for text_file in files:
    # Extract data structure from filename
    data_structure = Path(text_file).name.split('.txt')[0]
    
    # Read the data structure and capture all the elements from the file
    # Note this could have been done using the data returned from the NDA API
    # We are using pandas to read both the first and second rows of the file as the header
    # Note: by convention dataframe variables contain `df` in the name.
    data_structure_df = pd.read_table(text_file, header=[0, 1], nrows=0)
    for data_element, metadata in data_structure_df.columns.values.tolist():
        data_elements.append([data_element, metadata, data_structure])

    
    # (Optional) Retrieve the eventnames in each structure. Some structures were only collected
    # at baseline while others were collected at specific or multiple timepoints
    events_in_structure = None
    if any(['eventname' == data_element for data_element in data_structure_df.columns.levels[0]]):
        # Here we are skipping the 2nd row of the file containing desciption using skiprows
        possible_event_names_df = pd.read_table(fl, skiprows=[1], usecols=['eventname'])
        events_in_structure = possible_event_names_df.eventname.unique().tolist()
        event_names.update(events_in_structure)

    # (Optional) Retrieve the title for the structure using the NDA API
    rinfo = requests.get(f"https://nda.nih.gov/api/datadictionary/datastructure/{data_structure}").json()
    data_structures[data_structure] = StructureInfo(description=rinfo["title"] if "title" in rinfo else None,
                                                    eventnames=events_in_structure)

# Convert to a Pandas dataframe
data_elements_df = pd.DataFrame(data_elements, columns=["element", "description", "structure"])
```

We can use the `.head()` method of any DataFrame to quickly look at the first few entries
to make sure the DataFrame looks reasonable.
```python
data_elements_df.head()
```
#### Save data elements to a tab-separated file

In case we want to read/filter the data elements in 
another script so we do not need to run the above code again,
or share this information with someone, we can save the
data elements dataframe to a tab separated file (`tsv`).
**Note**: file extensions such as `tsv` and `txt` are markers for humans and certain computer programs to guess what the contents of a file are, but have no bearing on
what the content of a file are.
If a file was renamed from `data.txt` to `data.tsv`,
the contents of the file remain the same.
```python
data_elements_df.to_csv("data_elements.tsv", sep="\t", index=None)
```

The first number is the number of rows and the second number is the number of columns.
There are _a lot_ of data elements, but keep in mind some data elements like `subjectkey`
are shared across data structures in order to match observations across data structures.
```python
data_elements_df.shape
```

The number of data structures should match the number of txt files in the `data_path` directory.
```python
len(data_structures)
```

`event_names` contains all the unique timepoints represented across the data structures.
```python
event_names
```

#### Number of unique data elements
You should notice this number is less than
the number of rows in `data_elements_df`.
```python
data_elements_df.element.unique().shape
```

#### Example row entry in data elements dataframe
```python
data_elements_df.query("element == 'smri_vol_scs_amygdalalh'")
```

#### Find all data structures that have baseline data
We are interested in the baseline measures and not all
the data structures have a measure for baseline.
All data structures with a baseline measure will be
printed for your convience.

```python
NOEVENTS = {}
for data_structure, info in data_structures.items():
    if info.eventnames:
        if 'baseline_year_1_arm_1' in info.eventnames:
            print(f"{data_structure}: {info.description}")
    else:
        NOEVENTS[data_structure] = info
```

Structures with no eventname or no baseline measure.
We cannot choose data elements from these data structures
as they do not contain a baseline measure.

```python
for data_structure, info in NOEVENTS.items():
    print(f"{data_structure}: {info.description}")
```

#### Use the following code block to quickly introspect variables in a structure

```python
structure = 'abcd_mri01'  # 'abcd_psb01'
df = pd.read_table(data_path / f"{structure}.txt", header=[0, 1], nrows=0)
df.columns.tolist()
```

These are the data elements we require to answer our question of interest
(change these variables to match your research question of interest)
```python
common = ["subjectkey", "interview_date", "interview_age", "eventname", "sex"]
demographic = ["site_id_l", "anthroheightcalc", "anthroweightcalc", "ehi_y_ss_scoreb", 'neighborhood_crime_y', 'snellen_aid_y']
clinical = ['ksads_1_2_t', 'ksads_8_29_t', 'ksads_25_33_t', 'ksads_13_929_t', 'pps_y_ss_severity_score']
behavioral = ['prosocial_q2_y', 'prosocial_q3_y'] # 'fit_ss_sleepperiod_minutes', 'fit_ss_avg_hr_deep',
cognitive = []
imaging = ["smri_vol_cdk_total", "smri_vol_scs_amygdalalh", 'mri_info_manufacturer',]

data_elements_of_interest = demographic + clinical + behavioral + cognitive + imaging
```

#### Find the data structures that contain the elements

```python
structures2read = {}
for element in data_elements_of_interest:
    item = data_elements_df.query(f"element == {element}").structure.values[0]
    if item not in structures2read:
        structures2read[item] = []
    structures2read[item].append(element)
structures2read
```

#### Construct a new table of data containing the variables

```python
# Read data from one structure
df = pd.read_table(data_path / f"{list(structures2read)[0]}.txt", skiprows=[1], low_memory=False,
                  usecols=common + structures2read[list(structures2read)[0]])
df.head()
```

```python
all_df = None
count = 0
for structure, elements in structures2read.items():
    data_structure_filtered_df = pd.read_table(data_path / f"structure.txt", skiprows=[1], low_memory=False, usecols=common + elements)
    data_structure_filtered_df = data_structure_filtered_df.query("eventname == 'baseline_year_1_arm_1'")
    if all_df is None:
        all_df = df[["subjectkey", "interview_date", "interview_age", "sex"] + elements]
    else:
        all_df = all_df.merge(df[['subjectkey'] + elements], how='outer')
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
