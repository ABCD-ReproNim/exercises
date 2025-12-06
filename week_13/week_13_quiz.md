 Week 13 Quiz

### Quiz Instructions

In this Week 13 Data Exercise we will ask you a few questions about longitudinal data and longitudinal modelling ( you might have realized that both lectures are about that topic ;) 

***

### Section 1: Longitudinal Modeling Questions 1

First, we will ask you a few questions about longitudinal modeling, referring to the lecture of Dr Tara Madhyasta.

Note that, because code formatting is not a supported feature in Google Forms, we have made the following formatting choices:
1) All inline code is indicated via reverse apostrophes (e.g., `Hello World`)
2) Code blocks are indicated by three reverse apostrophes (e.g., ``` Hello World ```)
3) Terminal commands are indicated by the > symbol (e.g., > echo 'Hello World').
4) You can view a copyable version of all code related to this Data Exercise on our GitHub repository: https://github.com/ABCD-ReproNim/exercises/blob/main/week_13/week_13_quiz.md.

Additionally, this section of the quiz references a pre-written Jupiter notebook that will be used to answer some of the following questions. We will use git on the command line to fetch this notebook in a bit, but you can also view this notebook on GitHub here: https://github.com/ABCD-ReproNim/exercises/blob/main/week_13/linear_mixed_effects.md

If you have ABCD data access then we recommend you use a local version of  the ABCD-ReproNim Jupyterhub  in which the appropriate libraries used in the Notebook have already been installed (see our instructions on how to do this here: https://github.com/ABCD-ReproNim/exercises/blob/main/local_jupyter_hub.md or here https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439.)


**Question 1**

1) What makes a longitudinal design different from a cross-sectional design? (select all that apply)

- [ ] Multiple samples are collected over time from the same participant
- [ ] Longitudinal designs are not observational studies
- [ ] Better causal inference
- [ ] Removes concern from unmeasured variables


<details>
<summary>Click to see answer</summary>

- [x] Multiple samples are collected over time from the same participant
- [ ] Longitudinal designs are not observational studies
- [x] Better causal inference
- [ ] Removes concern from unmeasured variables

Longitudinal designs follow the same individuals repeatedly, allowing you to observe within-person change. Cross-sectional designs measure different people only once.

Because longitudinal designs track change over time, they help distinguish temporal ordering (“X happened before Y”), which improves—but does not guarantee—causal inference.

Longitudinal studies can absolutely be observational. Many large cohort studies (ABCD, ADNI, UK Biobank) are both longitudinal and observational.
Longitudinal designs reduce some confounding (because people serve as their own control), but unmeasured variables and confounding can still be a major issue.

</details>
***

**Question 2**

2) Imagine we are analyzing hippocampal volume over time, with 3 timepoints for each participant. Using R syntax, our model would be specified like so: `volume ~ time + (1 + time | subject)` Which of the following statements are True?

- [ ] `volume` is a fixed effect
- [ ] `time` is a fixed effect
- [ ] `time` is a random effect
- [ ] `subject` is a fixed effect
- [ ] `subject` is a random effect

<details>
<summary>Click to see answer</summary>

- [ ] `volume` is a fixed effect
- [x] `time` is a fixed effect
- [x] `time` is a random effect
- [ ] `subject` is a fixed effect
- [x] `subject` is a random effect

volume is a fixed effect — false
volume is the outcome/dependent variable, not an effect. Fixed vs. random effects refer to predictors, not the dependent variable.

time is a fixed effect — correct
time appears outside the parentheses in volume ~ time + (...), meaning we estimate a single population-level effect of time (the average slope across participants).
This is the fixed effect of time.

time is a random effect — correct
(1 + time | subject) specifies that each subject has their own intercept and their own slope for time.
So time also has a random slope, meaning the time effect varies between subjects.

subject is a fixed effect — false
If subject were a fixed effect, it would appear as + subject in the formula, treating each person as a separate group. We don’t do that here.

subject is a random effect — correct
(1 + time | subject) indicates that subject is the grouping factor for random effects.
This means subjects are considered a sample from a larger population, and we model their variability with random intercepts/slopes.

</details>
***

Next, let’s fetch a pre-written Notebook (viewable on GitHub here: https://github.com/ABCD-ReproNim/exercises/blob/main/week_13/linear_mixed_effects.md) we created that has example code for you to use in this next part of the assignment. This Notebook is meant as a fully executable guide that you can copy and paste code blocks from as you complete the questions we ask you below.

In your  local Hub environment, open In a Terminal window and use the following command to fetch the pre-written Notebook:

> wget https://raw.githubusercontent.com/ABCD-ReproNim/exercises/main/week_13/linear_mixed_effects.md

You can open `linear_mixed_effects.md` on the JupyterHub as a Notebook by right clicking the file then choosing "Open With" and "Notebook".

The simulated data can be interpreted as measuring brain volume from a particular area of interest (for example the hippocampus) over time. We are hypothesizing the brain area of interest increases in size over time, and we want to measure the average yearly increase of volume in our cohort. Run the code blocks in the notebook until you reach the section titled "Simple Dataset Conclusions".

**Question 3**

3) After you complete the Simple Dataset analysis, explain why the intercept is estimated to be `6940` (your answers may vary depending on the random seed) even though the baseline volume was simulated to be `7000`?

- [ ] Error inherent in model estimation
- [ ] 6940 represents the predicted volume at 0 months of age
- [ ] 6940 represents the predicted volume at 144 months of age
- [ ] 6940 represents the predicted volume at -12 months of age

<details>
<summary>Click to see answer</summary>
- [ ] Error inherent in model estimation
- [x] 6940 represents the predicted volume at 0 months of age
- [ ] 6940 represents the predicted volume at 144 months of age
- [ ] 6940 represents the predicted volume at -12 months of age 

</details>
***

***Question 4**

4) Also at the end of `Simple Dataset Conclusions`, answer this question about the models outputs. Which of the following is a correct interpretation of `interviewed_age`?

- [ ] for every month, volume has an estimated increase of 0.5 mm
- [ ] for every year, volume has an estimated increase of 0.5 mm
- [ ] for the first year, volume has an estimated increase of 0.5 mm
- [ ] for the last year, volume has an estimated increase of 0.5 mm

<details>
<summary>Click to see answer</summary>
- [x] for every month, volume has an estimated increase of 0.5 mm
- [ ] for every year, volume has an estimated increase of 0.5 mm
- [ ] for the first year, volume has an estimated increase of 0.5 mm
- [ ] for the last year, volume has an estimated increase of 0.5 mm 

</details>

***Question 5**

5) What are other random effects we should be aware of in the ABCD dataset when constructing models?

- [ ] sex
- [ ] site
- [ ] scanner
- [ ] age
- [ ] family 

<details>
<summary>Click to see answer</summary
- [ ] sex   
- [x] site
- [x] scanner
- [ ] age
- [x] family    

Site and scanner are important random effects to consider in ABCD, as data is collected across multiple locations and different scanner models/vendors. Family is also a critical random effect, as ABCD includes many siblings and twins, leading to non-independence of observations within families.

</details>

*** Section 2: Longitudinal Modeling Questions 2

These questions cover the lectures by Wes Thompson.

1) Select all that apply.

- [ ] Linear Mixed Effects Models can handle nested data structures.
- [ ] Generalized linear effects models are limited to modelling linear trends.
- [ ] Latent Growth Curve Models is a structural equation modelling approach that allows for modelling more complex structures.
- [ ] Mediation in longitudinal modelling decomposes the effect of an exposure into a direct and indirect pathway, and a moderator.
- [ ] Causal Mediation analysis requires more than two time points.

<details
<summary>Click to see answer</summary>
- [x] Linear Mixed Effects Models can handle nested data structures.
- [ ] Generalized linear effects models are limited to modelling linear trends.
- [x] Latent Growth Curve Models is a structural equation modelling approach that allows for modelling more complex structures.
- [ ] Mediation in longitudinal modelling decomposes the effect of an exposure into a direct and indirect pathway, and a moderator.
- [ ] Causal Mediation analysis requires more than two time points. 
</details>

2) In the context of missing values, select all statements that are true.

- [ ] Missing variables that are correlated with an analysis variable will not affect the outcome of the analysis.
- [ ] List-wise deletion does not affect the power of a study.
- [ ] For Multiple Imputation (MI), variables should be missing at random (MAR). Multiple data sets are created, which are then averaged.
- [ ] In Probability Score Weighting, samples are weighted based on the dropout rate of the population the sample is in.
- [ ] List-wise deletion is the preferred method to deal with structured missingness.
<details>
<summary>Click to see answer</summary>
- [ ] Missing variables that are correlated with an analysis variable will not affect the outcome of the analysis.
- [ ] List-wise deletion does not affect the power of a study.
- [x] For Multiple Imputation (MI), variables should be missing at random (MAR). Multiple data sets are created, which are then averaged.
- [x] In Probability Score Weighting, samples are weighted based on the dropout rate of the population the sample is in.
- [ ] List-wise deletion is the preferred method to deal with structured missingness. 
</details>

3) Select all statements that are true.

- [ ] The ABCD study is an observational study, hence all exposures were randomly assigned.
- [ ] The analysis of monozygotic and dizygotic twins allows to disentangle the effects of genes versus environment on a trait of interest.
- [ ] Dizygotic twins provide counterfactuals of each other.
- [ ] Due to the large sample size in ABCD, small group differences become hardly ever statistically significant.
- [ ] Due its large sample size, ABCD allows for causal conclusions from correlational analyses.

<details>
<summary>Click to see answer</summary>
- [ ] The ABCD study is an observational study, hence all exposures were randomly assigned.
- [x] The analysis of monozygotic and dizygotic twins allows to disentangle the effects of genes versus environment on a trait of interest.
- [ ] Dizygotic twins provide counterfactuals of each other.
- [ ] Due to the large sample size in ABCD, small group differences become hardly ever statistically significant.
- [ ] Due its large sample size, ABCD allows for causal conclusions from correlational analyses. 
</details>  




