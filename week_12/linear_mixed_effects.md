---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Week 12 Part 1: Longitudional Modeling

You will use this notebook to answer questions from the longitudional modeling portion of in the Week 12 quiz.

# Linear Mixed Effect Models

In the following notebook we will explore:
- data simulation
- mixed effects models
- within and between subject variance
- model interpretation

The simulated data that we will create in this exercise can be interpreted as measuring brain volume from a particular area of interest (for example the hippocampus) over time.
We may guess the brain area of interest increases in size over time, and we want to measure the average yearly increase of volume in our cohort.
First let's import all of the libraries that we will need.


```python
from copy import deepcopy # to deep copy data
import pandas as pd # to work with tabular data
import numpy as np # to generate random numbers and perform computations on numbers
import statsmodels.formula.api as smf # to fit mixed (i.e., fixed and random) effects models
import seaborn as sns # plot data
```


```python
# ignoring warnings for this lesson to narrow focus on concepts
import warnings
warnings.filterwarnings('ignore')
```

## Functions

Below are the functions used to simulate, plot, and analyze data respectively.
By wrapping up common code into functions, we make it easier to change the code
and call it repeatedly without rewriting all the code. 
If you're not familiar with defining your own functions in Python [this](https://realpython.com/defining-your-own-python-function/) 
is a good tutorial to check out.


```python
# number of months in a year
MONTHS = 12
BASELINE_AGE = 10 * MONTHS # 10 years old

def generate_data(groups, timepoints, rng):
    """
    Parameters
    ----------
    groups : dict of dicts
        dictionary providing specific attributes of the data.
        The top level dictionary defines the groups, and the
        sub-dictionaries describe how to simulate the data:
        - mean: average simulated volume
        - variance: variance of the simulated volume
        - baseline_age: age to use as reference to interpret the intercept
        - n: number of participants
        - year_growth: yearly growth of volume
        - growth_wthn_variance: variance of the volume growth within an individual
        - growth_btwn_variance: variance of the volume grown between individuals
    timepoints : int
        number of timepoints to simulate
    rng : np.random.Generator
        random number generator to ensure reproducibility
    
    Returns
    -------
    df : pandas.DataFrame
        A long form DataFrame with the simulated data.
    """
    dfs = []
    for name, group in groups.items():
        # generate the volumes at baseline (different participants may have different baselines/intercepts)
        baseline_means = rng.normal(group['mean'], np.sqrt(group['variance']), group['n'])
        # determine the growth trajectory for each participant
        growth = rng.normal(group['year_growth'], np.sqrt(group['growth_btwn_variance']), group['n'])
        # add the growth trajectory to the baseline volume (different participants may have different trajectories/slopes)
        baseline_growth = np.linspace(baseline_means, baseline_means + (growth * (timepoints - 1)), timepoints)
        # add the within subject variance (participants may not follow their trajectory perfectly)
        wthn_subj_growth_variance = rng.normal(0, np.sqrt(group['growth_wthn_variance']), (timepoints, group['n']))
        # add the between and within subject variances together
        group_data = baseline_growth + wthn_subj_growth_variance
        
        # create column names for the dataframe
        columns = np.linspace(BASELINE_AGE, BASELINE_AGE + (MONTHS * (timepoints - 1)), timepoints)
        column_names = [f'volume-{int(age)}' for age in columns]
        
        # create a temporary dataframe
        tmp_df = pd.DataFrame(group_data.T, columns=column_names)
        tmp_df['group'] = [name] * tmp_df.shape[0]
        dfs.append(tmp_df)
    # combine all the groups into a single dataframe
    full_df = pd.concat(dfs, ignore_index=True)
    
    # transform the dataframe to long (from wide) format for analysis
    long_df = pd.wide_to_long(full_df.reset_index(), stubnames='volume', i='index', j='interview_age', sep='-')
    long_df = long_df.reset_index().rename(columns={'index': 'subjectkey'}).sort_values(by=['subjectkey', 'interview_age'], ignore_index=True)
    
    # demean the interview age (for a homework question)
    long_df['interview_age_demeaned'] = long_df['interview_age'] - group['baseline_age']
    return long_df
    

def plot_sample_data(df, n_participants=4):
    """
    Plots data for a subset of participants
    """
    sns.lmplot(
        x="interview_age",
        y="volume",
        col="subjectkey",
        hue="subjectkey",
        data=df[df['subjectkey'].isin(range(n_participants))],
        col_wrap=2,
        ci=None,
        palette="muted"
    )    
    

def analyze_data(df):
    """
    Runs:
    - a linear model
    - linear mixed model with random intercepts for participants
    - linear mixed model with random intercepts and slopes for participants
    """
    
    lm = smf.ols("volume ~ interview_age", df)
    lmf = lm.fit()
    print("Simple Linear Model (volume ~ interview_age)")
    print(lmf.summary())
    print("\n\n")
    
    mi = smf.mixedlm("volume ~ interview_age", df, groups="subjectkey")
    try:
        mif = mi.fit(method=["lbfgs"])
    except:
        print("Could Not Fit Mixed Effects Intercepts Model\n\n")
    else:
        print("Mixed Effects Model with intercept for 'subjectkey' (volume ~ interview_age + (1 | subjectkey))")
        print(mif.summary())
        print("\n\n")
    
    
    mis = smf.mixedlm("volume ~ interview_age", df, groups="subjectkey", re_formula="~interview_age")
    try:
        misf = mis.fit(method=["lbfgs"])
    except:
        print("Could Not Fit Mixed Effects Intercepts and Growth Model\n\n")
    else:
        print(("Mixed Effects Model with intercept for 'subjectkey' and slope for 'interview_age'" 
               "(volume ~ interview_age + (1 + interview_age | subjectkey))"))
        print(misf.summary())
        print("\n\n")
    
    
```


```python
# want 3 timepoints
timepoints = 3
```

## Simple Dataset

In the simple dataset we simulate below, every participant has the same starting point (7000) and the same growth trajectory (6) which they follow perfectly.
In essence, each person is a clone that follows a deterministic growth trajectory.

Since there is not any variance to be accounted for, a simple ordinary least squares analysis is most appropriate.


```python
simple_group = {
    'control': {
        'mean': 7000,
        'variance': 0,
        'baseline_age': 120,
        'n': 200,
        'year_growth': 6,
        'growth_wthn_variance': 0,
        'growth_btwn_variance': 0,
    }
}
rng = np.random.default_rng(seed=123)
simple_df = generate_data(simple_group, timepoints, rng)
```


```python
simple_df.head(n=9) # all participants look the same
```


```python
plot_sample_data(simple_df) # all participants look the same
```


```python
analyze_data(simple_df)
```

### Simple Dataset Conclusions
One of the mixed effects models cannot even be run since there is no variance and the output of another is missing key values since there is no between subject variance to estimate.
Only ordinary least squares computes sensibly with a coefficient of `0.5 mm^3`.
Since the unit of time is in months, increasing volume by `0.5 mm^3` a month results in a `6.0 mm^3` annual increase, exactly what was specified in our simulated data. 

### Intercept Question

Why is the intercept 6940? The baseline average volume was set to be 7000, where is the value 6940 coming from?

## Varying Intercepts Dataset

Next, in the following simulated dataset, each participant has a different starting point/baseline, but 
they still all follow the same trajectory perfectly.
Including random intercepts helps model the varying intercepts between participants.


```python
intercepts_group = deepcopy(simple_group)
intercepts_group['control']['variance'] = 1000
rng = np.random.default_rng(seed=123)
diff_intercepts_df = generate_data(intercepts_group, timepoints, rng)
```


```python
diff_intercepts_df.head(n=9) # the intercepts vary
```


```python
plot_sample_data(diff_intercepts_df) # the intercepts vary
```


```python
analyze_data(diff_intercepts_df)
```

In the simple ordinary least squares model, the variance from the intercepts becomes a part of the standard error of the estimate (within subject error), reducing the overall significance of the `interview_age` statistic.
The random intercept mixed effect model, on the other hand, properly attributes the varying intercepts as between subject variance instead of within subject variance, increasing the power of the test.
Since the slopes do not vary between participants in the current simulated dataset, though, a random intercepts plus slopes model would not give the test more power (and may make the equation non-estimable).

## Varying Intercepts and Slopes

We have seen the impact of varying intercepts between participants on the estimation of annual volume increases and in this next segment we will vary individual participant slopes as well.
Some participants may have their brain volume increase slowly, and others may have decreases in brain volume, but the average increase of `6 mm` a year stays the same. 


```python
intercepts_and_growth_group = deepcopy(intercepts_group)
intercepts_and_growth_group['control']['growth_btwn_variance'] = 1000
rng = np.random.default_rng(seed=123)
diff_intercepts_and_growth_df = generate_data(intercepts_and_growth_group, timepoints, rng)
```


```python
diff_intercepts_and_growth_df.head(n=9)
```


```python
plot_sample_data(diff_intercepts_and_growth_df) # intercepts and slopes differ
```


```python
analyze_data(diff_intercepts_and_growth_df)
```

### Varying Intercepts and Slopes Conclusions

The mixed effects model that includes a random intercept and slope `(1 + interview_age | subject)` is the most powerful since the data were created with varying intercepts and slopes.

## Within Subject Variance

By varying intercepts and slopes, we were increasing "between" subject variation, but we have not yet touched on "within" subject variation.
You can think of "within" subject variation as "how far am I off my line today?".
In all the previous plots, the data points for each participant were exactly on their line,
in this next dataset, we will push their data points away from their line.
We will not say much about this analysis, but it is included for completeness to understand
the sources of variance when fitting a mixed effects model.


```python
all_variance_group = deepcopy(intercepts_and_growth_group)
all_variance_group['control']['growth_wthn_variance'] = 1000
rng = np.random.default_rng(seed=123)
all_variance_df = generate_data(all_variance_group, timepoints, rng)
```


```python
all_variance_df.head(n=9) # intercepts, slopes, and individual points vary
```


```python
plot_sample_data(all_variance_df)
```


```python
analyze_data(all_variance_df)
```

## Conclusions

- Sources of variance can come from between subject factors (intercepts and slopes in our example) as well as within subject factors ("how far am I off my line today?").
- Depending on the where the variance is, the appropriate model may change (no random effects, random intercept, or random intercept plus slope).
- Intercepts can change their meaning depending on how your independent variable is coded.

## Further Resources

- A much better (but slightly less relevant) [mixed effects modeling simulator](https://shiny.psy.gla.ac.uk/lmem_sim/)
and [associated tutorial](https://debruine.github.io/lmem_sim/articles/paper.html)
- [Another wonderful visualization of random intercepts and slopes](http://mfviz.com/hierarchical-models/)
