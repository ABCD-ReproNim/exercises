# Week 12 Quiz

### Quiz Instructions

In this Week 12 Quiz, we will ask you a few questions about [Longitudinal Models
and Machine Learning](https://abcd-repronim.github.io/materials/week-12/).

***

## ABCD questions

**Question 1**

What makes a longitudinal design different from a cross-sectional design?
(select all that apply)

- [ ] Multiple samples are collected over time from the same participant
- [ ] Longitudinal designs are not observational studies
- [ ] Better causal inference
- [ ] Removes concern from unmeasured variables

<details>
<summary>Click to see answer</summary>

- [x] Multiple samples are collected over time from the same participant
  - Cross sectional designs only collect samples at one time point.
- [ ] Longitudinal designs are not observational studies
  - There is no inherit intervention in longitudinal studies making them observational as well.
- [x] Better causal inference
  - ["Longitudinal data have the ability to establish temporal precedence, thus improving
    causal inference over cross-sectional studies because observations of an outcome at a
    prior time point may be controlled."](https://www.sciencedirect.com/science/article/pii/S1878929317300300)    
- [ ] Removes concern from unmeasured variables
  - ["As with cross-sectional data, longitudinal data can suffer from unmeasured third variables that confound causality"](https://www.sciencedirect.com/science/article/pii/S1878929317300300)


***

</details>

**Question 2**

Imagine we are analyzing hippocampal volume over time, with 3 timepoints
for each participant. Using `R`s syntax, our model would be specified like so:
`volume ~ time + (1 + time | subject)`
Which of the following statements are **True**?

- [ ] `volume` is a fixed effect
- [ ] `time` is a fixed effect
- [ ] `time` is a random effect
- [ ] `subject` is a fixed effect
- [ ] `subject` is a random effect

<details>
<summary>Click to see answer</summary>

- [ ] `volume` is a fixed effect
  - `volume` is the dependent/outcome variable.
- [x] `time` is a fixed effect
  - The main effect of `time` is being estimated.
- [x] `time` is a random effect
  - `subjects` are given random slopes meaning the variance in their growth
    over `time` is being estimated. 
- [ ] `subject` is a fixed effect
  - `subject` does not appear in the fixed effect portion of the equation.
- [x] `subject` is a random effect
  - `subject` is the grouping variable for which we have multiple observations
    over time.

***

</details>

**Question 3**

Next, let’s fetch a pre-written Notebook we created that has example code for you to use in the next part of the assignment. This Notebook is meant as a fully executable guide that you can copy and paste code blocks from as you complete the questions we ask you below. 

$ wget https://raw.githubusercontent.com/ABCD-ReproNim/exercises/main/week_12/linear_mixed_effects.md

You can open `linear_mixed_effects.md` on the JupyterHub as a Notebook by right clicking the file then choosing "Open With" and "Notebook".

The simulated data can be interpreted as measuring brain volume from a particular area of interest (for example the hippocampus) over time.
We are hypothesizing the brain area of interest increases in size over time, and we want to measure the average yearly increase of volume in our cohort.
Run the code blocks in the notebook until you reach `Simple Dataset Conclusions`.
After you complete the Simple Dataset analysis, explain why the intercept
is estimated to be `6940` even though the baseline volume was simulated to be `7000`?

- Error inherent in model estimation
- `6940` represents the predicted volume at `0` months of age
- `6940` represents the predicted volume at `144` months of age
- `6940` represents the predicted volume at `-12` months of age

<details>
<summary>Click to see answer</summary>

`6940` represents the predicted volume at `0` months of age

We should think about the meaning of our intercepts and whether they make sense to
us.
It may make more sense if the intercept was 9 or 10 years old since that would represent
the earliest observed data in our dataset.
Extrapolating to 0 years old does not make much sense because we did not measure anyone
at 0 years old, and it may be implausible to assume a linear model from 0 -10 years old.

***

</details>

**Question 4**

Also at the end of `Simple Dataset Conclusions`, answer this question
about the models outputs.
Which of the following is a correct interpretation of `interviewed_age`?

- for every month, volume has an estimated increase of `0.5 mm`
- for every year, volume has an estimated increase of `0.5 mm`
- for the first year, volume has an estimated increase of `0.5 mm`
- for the last year, volume has an estimated increase of `0.5 mm`

<details>
<summary>Click to see answer</summary>

- for every month, volume has an estimated increase of `0.5 mm`

`interview_age` is represented in months meaning the parameter
represents monthly change.
The simulation, however, represents the change in years, so
a `6 mm` yearly change becomes a `0.5 mm` monthly change (`6 / 12 = 0.5`).

***

</details>

**Question 5**

What are other random effects we should be aware of in the ABCD dataset
when constructing models?

- [ ] sex
- [ ] site
- [ ] scanner
- [ ] age
- [ ] family



<details>
<summary>Click to see answer</summary>

- [ ] sex
- [x] site
- [x] scanner
- [ ] age
- [x] family

***

</details>
