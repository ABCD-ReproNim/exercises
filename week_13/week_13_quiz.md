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