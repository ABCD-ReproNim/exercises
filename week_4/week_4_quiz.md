# Week 4 Quiz 

### Quiz Instructions

In this Week 4 Quiz, we will ask you a few questions about ABCD (Imaging Measures) and you will complete a few ReproNim exercises (Pre-Registration and P-Hacking).

*** 

### ABCD Questions 

**Question 1**

The ABCD scanning protocol includes the following types of images:

- [ ] T1w, T2w, resting-state fMRI; task-based fMRI
- [ ] T1w; T2w; diffusion weighted imaging (DWI), resting-state fMRI
- [ ] T1w; T2w; DWI; resting-state fMRI; task-based fMRI
- [ ] T1w; T2w; DWI; resting-state fMRI; task-based fMRI; arterial spin labeling (ASL) 

<details>
<summary>Click to see answer</summary>

T1w; T2w; DWI; resting-state fMRI; task-based fMRI

***

</details>

**Question 2**

The ABCD tasks were selected based on (check all that apply):

- [ ] Validity and feasibility
- [ ] Sensitivity and specificity
- [ ] Reliability and generalizability

<details>
<summary>Click to see answer</summary>

Validity and feasibility

Sensitivity and specificity

Reliability and generalizability

***

</details>


**Question 3**

Before ABCD data are made available on NDA, the images are subject to (check all that apply):

- [ ] Compliance check for completeness and sanity checks
- [ ] Quality checks that are computed automatically (e.g., mean framewise displacement)
- [ ] Quality checks performed manually by reviewers who inspect all images pre- and post-processing
- [ ] Nothing. Poor quality participant data are automatically excluded on NDA

<details>
<summary>Click to see answer</summary>

Compliance check for completeness and sanity checks

Quality checks that are computed automatically (e.g., mean framewise displacement)

Quality checks performed manually by reviewers who inspect all images pre- and post-processing

***

</details>

**Question 4**

ABCD Study neuroimaging data that have been minimally processed can be accessed via (check all that apply):

- [ ] NDA Fast Track data
- [ ] NDA Tabulated data
- [ ] ABCD-BIDS Community Collection 3165

<details>
<summary>Click to see answer</summary>

NDA Tabulated data

ABCD-BIDS Community Collection 3165

***

</details>


**Question 5**

Brain-wide association studies (BWAS) detecting small effect sizes require large datasets to ensure reliability.

- [ ] True
- [ ] False

<details>
<summary>Click to see answer</summary>

True

***

</details>

**Question 6**

To take account "nested" covariates in ABCD study, which statistical approach is recommended:

- [ ] General Linear Modeling
- [ ] Mixed Effect Modeling
- [ ] Marginal Modeling using the Sandwich Estimator For Neuroimaging Data

<details>
<summary>Click to see answer</summary>

Marginal Modeling using the Sandwich Estimator For Neuroimaging Data

***

</details>

### ReproNim Questions 

Now we will ask some statistical questions relevant to Pre-Registration and P-Hacking

**Question 6**

Please select all the statements that are true of p-values (check all that apply):

- [ ] A p-value allows one to decide to what extent a model is not compatible with the data being analyzed.
- [ ] A p-value is sufficient to compute the effect size.
- [ ] A p-value reflects the probability of rejecting the null hypothesis.
- [ ] A p-value and other relevant statistical measures should not be reported separately or selectively.

<details>
<summary>Click to see answer</summary>

A p-value allows one to decide to what extent a model is not compatible with the data being analyzed.

A p-value and other relevant statistical measures should not be reported separately or selectively.

*** 
</details>

**Question 7**

Which type of effect size allows you to infer how meaningfully small or big an effect is?

- [ ] Non-standardized
- [ ] Standardized
- [ ] Both

<details>
<summary>Click to see answer</summary>

Standardized

*** 
</details>

**Question 8**

A researcher conducts a study where she compares two groups using an independent t-test and finds that they are significantly different (at the .05 level) with respect to a variable of interest. However, the power of the study is estimated at 0.25. What conclusion can the researcher draw?

- [ ] The detected effect is likely over-estimated due to estimation uncertainties
- [ ] The detected effect is under-estimated due to the true positive rate being high.
- [ ] It depends on the variable of interest.

<details>
<summary>Click to see answer</summary>

The detected effect is likely over-estimated due to estimation uncertainties

*** 
</details>

**Question 9**

This same researcher wants to compute the sample size needed to detect a standardized effect size of 0.4 when the Type II error is 0.2. The significance level used for this study is the standard 0.05. Given these parameters, what is the required total sample size for this study if the two groups of interest are equally sized? Hint: you can compute this by hand or use the Python statsmodels library/R stats library. 

- [ ] 154
- [ ] 198
- [ ] 50
- [ ] 310

<details>
<summary>Click to see answer</summary>

Both R and Python can be used to solve this problem and get the answer for the sample size of ONE of the groups, i.e. to get the final answer, we need to multiply the answer by two since we know the groups are equally sized. 

**Solution in Python**

```
> from statsmodels.stats.power import tt_ind_solve_power
> tt_ind_solve_power(effect_size=0.4, alpha=0.05, power=0.8, alternative='two-sided')
99.08032683981143
```

Note: The [statsmodels](https://www.statsmodels.org/stable/index.html) package is a really handy Python library for all sorts of statistical modelling. The `tt_ind_solve_power` function allows you to solve for any parameter 
of the power of a two sample t-test so long as the other parameters are provided. As with the analogous R function, the value returned for `n` is the sample size for one of the groups.

**Solution in R**
```
> library(pwr)
> pwr.t.test(d=0.4, power=0.8, sig.level=0.05)
    Two-sample t test power calculation 
            n = 99.08032
            d = 0.4
    sig.level = 0.05
            power = 0.8
    alternative = two.sided
NOTE: n is number in *each* group
```

Note: In R the `pwr` library can be used in much the same way that the `stats.power` submodule from `statsmodels` is used. 

*** 
</details>

**Question 10**

Which of these can affect the validity of a study's results?

- [ ] Failing to control for bias when designing a study
- [ ] Having insufficient statistical power to detect an effect
- [ ] Using an inappropriate statistical test to analyze the data that have been collected
- [ ] Not correcting for multiple comparisons
- [ ] All the above

<details>
<summary>Click to see answer</summary>

All the above

*** 
</details>
