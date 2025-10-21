# Week 7 Quiz

### Quiz Instructions

In this Week 7 Data Exercise, we will ask you a few questions about ABCD friends, family, and community assessments (https://www.youtube.com/watch?v=EbHXALb484k&t=2171s) and some questions about scientific questions and statistical issues (https://youtu.be/auzLLbQPMfY).

***

## ABCD questions

**Question 1**

1) Which general parameters were considered when deciding which friends, family, and community factors to include in the ABCD Study (select all that apply)?

- [ ] Being a component in the PhenX toolkit
- [ ] Time to administer
- [ ] Validity across cultures
- [ ] Racial and ethnic group classifications that align with census groups

<details>
<summary>Click to see answer</summary>

- Being a component in the PhenX toolkit
- Time to administer
- Validity across cultures

***

</details>

**Question 2**

2) The ABCD Study aimed to recruit a certain percentage of participants from a "high risk" group, where high risk is identified as a likelihood to use marijuana by age 14-15 and measured using a screening developed by Loeber et al, 2018. What was the recruitment goal for this "high risk" group?

- 40%
- 45%
- 50%
- 55%
- 60%


<details>
<summary>Click to see answer</summary>

- 50%

***

</details>

**Question 3**

3) The friends, family, and community component of the ABCD protocol has a modest ability to differentiate between these higher and lower risk groups. For the baseline data, 64% of the tests of difference between the higher and lower risk groups are significant. How many of these tests make the 0.20 cut-off for a meaningful effect size?

- None
- 2
- 4
- 7


<details>
<summary>Click to see answer</summary>

- 4

***

</details>

**Question 4**

4) With one exception, in the friends, family, and community component of the ABCD Study, the baseline parent and youth reports all show the same patterns with the regard to sex differences. For which measure was the sex difference (or lack thereof) found in the youth report not found in the parent report?

- [ ] Neighborhood Safety
- [ ] FES Conflict subscale
- [ ] SDQ Prosocial Behavior
- [ ] Parental Monitoring

<details>
<summary>Click to see answer</summary>

- Neighborhood Safety

***

</details>

**Question 5**

5) Which of the following measures were administered for the first time at the one-year follow-up assessment for youth (select all that apply)?

- [ ] PhenX Neighborhood Safety/Crime
- [ ] Perceived Discrimination Scale
- [ ] Prosocial Tendencies
- [ ] Wills Problem Solving

<details>
<summary>Click to see answer</summary>

- Perceived Discrimination Scale
- Wills Problem Solving
  
***

</details>

## ReproNim questions

**Question 6**

Researcher 1 has published the results of a study. Since then the most recent version of the analysis software has changed. They want to see if their results hold with the new software version.

Researcher 2 wants to see if Researcher 1’s results hold in a different dataset. They use the same software and code for the analysis.

If the results hold in both scenarios, which of the following are true of the primary study’s results?


- They are generalizable and robust
- They are robust and replicable
- They are reproducIble and robust 
- They are reproducible and replicable


<details>
<summary>Click to see answer</summary>

- They are robust and replicable

***

</details>

**Question 7**

The positive predictive value depends on which of the following values (select all that apply)?

- [ ] Type I error
- [ ] Type II error
- [ ] Probability of alternative hypothesis
- [ ] Probability of null hypothesis
- [ ] Power


<details>
<summary>Click to see answer</summary>

- Type I error
- Probability of alternative hypothesis
- Probability of null hypothesis
- Power

***

</details>

**Question 8**

Statement 1: Participants were more rewarded in condition A because the ventral striatum showed greater activity

Statement 2: Trials where participants reported greater subjective reward were associated with greater activity in the ventral striatum. 

Which of the following is true (select all that apply)?

- [ ] Statement 1 is a forward inference.
- [ ] Statement 1 is a reverse inference.
- [ ] Statement 2 is a forward inference.
- [ ] Statement 2 is a reverse inference.

<details>
<summary>Click to see answer</summary>

- Statement 1 is a reverse inference.
- Statement 2 is a forward inference.

***

</details>

**Question 9**

Which is true of predictive modeling (select all that apply)?

- [ ] Improves theoretical accuracy
- [ ] Minimizes the combination of bias and estimation variance
- [ ] Primarily cares about accuracy
- [ ] Obtains the most accurate representation of the underlying theory

<details>
<summary>Click to see answer</summary>

- Minimizes the combination of bias and estimation variance
Primarily cares about accuracy

***

</details>

**Question 10**

For this question you will need some data with which to explore the relationships between sample size and the different measures of effect size discussed in this week's lecture. We have simulated a dataset for you to use that is based on [ABCD structural MRI morphometric and image intensity measures ("abcd_smrip201")](https://nda.nih.gov/data_structure.html?short_name=abcd_smrip201) data file. These data represent the sum total volume of both the left and right hippocampi across 10000 participants. You can download our simulated data file for this assignment [on our GitHub](https://github.com/ABCD-ReproNim/exercises/blob/main/week_7/simulated_data.tsv) or simulate it yourself. Alternatively, if you have ABCD data access, feel free to work directly with the data (the answers you will compute should end up being the same).

First, in your favorite programming language (we like Python), either read in the [simulated data file](https://github.com/ABCD-ReproNim/exercises/blob/main/week_7/simulated_data.tsv) (option A), simulate the data yourself (option B), or download and parce the appropriate ABCD data elements from [abcd_smrip201](https://nda.nih.gov/data_structure.html?short_name=abcd_smrip201) (option C).


*Option A: read in data from [our GitHub](https://github.com/ABCD-ReproNim/exercises/blob/main/week_7/simulated_data.tsv)*
```
import requests
import io
import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/ABCD-ReproNim/exercises/main/week_7/simulated_data.tsv" 
# Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe
hippo = pd.read_csv(io.StringIO(download.decode('utf-8')), sep='\t')
```

*Option B: simulate data using on the mean and standard deviation of hippocampal values*
```
# male
m_mean = 8407
m_std = 813
m_vol = np.random.normal(m_mean, m_std, 5000)
m_dat = pd.DataFrame(m_vol, columns=['hippocampi'])
m_dat['sex'] = 'M'
m_dat.head()

# female
f_mean = 7892
f_std = 775
f_vol = np.random.normal(f_mean, f_std, 5000)
f_dat = pd.DataFrame(f_vol, columns=['hippocampi'])
f_dat['sex'] = 'F'
f_dat.head()

# concatenate
hippo = pd.concat([m_dat, f_dat])
```

*Option C: read in and parce ABCD data using on the mean and standard deviation of hippocampal values*
```
# import full data -- note you will need to download this data from the NDA directly
To download and parse the data on your own if you have data acces, go to the NBDC data hub, login and go to lasso infomatics. Create a query in the dictionary
query tool and include these 3 pieces:

1) mr_y_smri__vol__aseg__hc__lh_sum #select section 00A
3) mr_y_smri__vol__aseg__hc__rh_sum #select section 00A
4) ab_g_stc__cohort_sex

You will be able to download all three of these as a single csv file and follow the next steps to parse the dataset:

import requests
import io
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

smrip201 = pd.read_csv("DATASETNAME") #copy and paste the name of the dataset in place of DATASETNAME and enclose the name in quotes

# subset to only include columns of interest
columns = ['participant_id','ab_g_stc__cohort_sex','mr_y_smri__vol__aseg__hc__lh_sum','mr_y_smri__vol__aseg__hc__rh_sum']
hippo = smrip201.loc[:,columns]
# sum left and right hippocampi
hippo['hippocampi'] = hippo['mr_y_smri__vol__aseg__hc__lh_sum'] + hippo['mr_y_smri__vol__aseg__hc__rh_sum']
# make names easier to read
hippo.rename(columns={'mr_y_smri__vol__aseg__hc__lh_sum':'left','mr_y_smri__vol__aseg__hc__rh_sum':'right', 'ab_g_stc__cohort_sex':'sex'},inplace=True)
```

Now that you have the total hippocampal volume for both male and female participants, we can subset these data at multiple sample sizes to see the relationship between effect size and sample size. The goal is to get a distribution of effect sizes corresponding to each sample size we choose. We can then use these distributions to visualize how the mean effect sizes may change as a function of sample size.

We want to give you the opportunity to practice coding, so try to do the following on your own:

1) Create a vector of sample sizes beginning at 10 and ending at 1000, with increments of 20 (so, 50 different sample sizes). 
2) For each sample size, loop through a large number of iterations (eg, 1000) of subsetting the full male and female participant data so that each iteration has a subset where the number of male and female participants equals the sample size. 
3) For each iteration, calculate the raw effect size (e.g., the difference of the two sample means), the Cohen’s d, and the z-scored Cohen’s d. Also make sure to record the sample size for each iteration. 
4) Now calculate these values for each sample size with your specified number of iterations. For 1000 iterations over 50 sample sizes, this took ~8 minutes on the JupyterHub.

Here is a function you can use to calculate the effect sizes (step 3):
```
# Function to calculate effect size for a given sample size
def eff_size_cal(df, niter, n_size):
    raw_eff = []
    cohen = []
    z = []
    for i in range(niter):
        male = df[df['sex']=='M'].sample(n_size) #if you downloaded the data yourself change 'M' to 1, with no quotes, sex is an integer not a string in this case
        female = df[df['sex']=='F'].sample(n_size) #if you downloaded the data yourself change 'F' to 2, with no quotes, sex is an integer not a string in this case
        m_mu = male['hippocampi'].mean()
        f_mu = female['hippocampi'].mean()
        #pooled standard deviation for males and females
        # here: same number of male and female, hence just averaging the two variance
        # if not same sample size, do a proportional weighting
        pooled_var = ((male['hippocampi'].std())**2 + (female['hippocampi'].std())**2)/2
        sigma = math.sqrt(pooled_var)
        raw_eff.append(m_mu - f_mu)
        cohen.append((m_mu - f_mu)/sigma)
        # to be exact, variance of the difference of the means : v(m - f) = v(m) + v(f) - 2cov(f,m) 
        # we assume data are independant between m and f
        # hence v(m-f) = 2*sigma**2 / n_size 
        z.append( ((m_mu - f_mu)/(math.sqrt(2)*sigma)) / math.sqrt(n_size))
        
    results = pd.DataFrame(list(zip(raw_eff,cohen,z)), columns=['raw_eff','cohen','z'])
    results['n'] = n_size
    
    return results
```
  
When you are finished calculating the numbers, plot the results. You’ll need three plots, one for the distributions of raw effect size, cohen’s d, and z-scored cohen’s d for each sample size you iterated over.

According to your results, as sample size increases which of the following are generally true (more or less, there will be variability across iterations). 

- Raw effect decreases, cohen’s d increases, z increases
- Raw effect stays the same, cohen’s d stays the same, z decreases
- Raw effect stays the same, cohen's d increases, z stays the same

NOTE: remmeber your plots should show a *distribution* of effect sizes at each sample size. You should focus on if the *means* of the effect size distributions changes with each sample size step.

<details>
<summary>Click to see answer</summary>

- Raw effect stays the same, cohen’s d stays the same, z decreases

see [code](https://github.com/ABCD-ReproNim/exercises/blob/main/week_7/week_7_year_2_data_and_solution.py) in `exercises/week_7` for a solution

</details>
