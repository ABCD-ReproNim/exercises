# Week 7 Quiz

### Quiz Instructions

In this Week 7 Quiz, we will ask you a few questions about the ABCD Demographic, Physical, and Mental Health Assessments and Scientific Questions and Statistical Issues.

***

## ABCD questions

**Question 1**

ABCD mental and physical health assessments include measures related to the following domains: (select all that apply)

- [ ] Categorical diagnoses and dimensional measures of mental health
- [ ] Trait-like behaviors and personality measures associated with risk factors and consequences of mental health outcomes 
Stress, life events (e.g., COVID-19), and peer environment (e.g., friendships and bullying)
- [ ] Blood draws and saliva samples for genetic and hormone testing
- [ ] Nutrition, physical activity, and actigraphy (fitbit) data
- [ ] Baby teeth for determining early exposure to toxins

<details>
<summary>Click to see answer</summary>

- Categorical diagnoses and dimensional measures of mental health
- Trait-like behaviors and personality measures associated with risk factors and consequences of mental health outcomes 
Stress, life events (e.g., COVID-19), and peer environment (e.g., friendships and bullying)
- Blood draws and saliva samples for genetic and hormone testing
- Nutrition, physical activity, and actigraphy (fitbit) data
- Baby teeth for determining early exposure to toxins

***

</details>

**Question 2**

What are some of the key challenges and considerations pertaining to the design of the ABCD health assessment? (select all that apply)

- [ ] Collecting measures that are consistent across visits versus measures that are relevant for different stages of development
- [ ] Utilizing reliable and valid instruments that are known to be relevant given prior literature versus opportunities that allow for discovery science
- [ ] Obtaining both child and parent blood draws required by the study
- [ ] Keeping participant burden in mind so to ensure retention over the course of the study


<details>
<summary>Click to see answer</summary>

- Collecting measures that are consistent across visits versus measures that are relevant for different stages of development
- Utilizing reliable and valid instruments that are known to be relevant given prior literature versus opportunities that allow for discovery science
- Keeping participant burden in mind so to ensure retention over the course of the study

***

</details>

**Question 3**

Parent and child reports are frequently inconsistent with one another. One way in which a researcher may evaluate the convergent validity of certain domains (e.g., problem behavior) is through teacher reports.

- True
- False


<details>
<summary>Click to see answer</summary>

- True

***

</details>

**Question 4**

What are some of the main goals of interviewing the parent (in addition to the child) about themselves and the child? (select all that apply)

- [ ] Parents may be able to report about certain domains such as externalizing symptoms more accurately than the child
- [ ] Parents have greater access to knowledge of family history
- [ ] Parent mental health may color their reports of the child
- [ ] To allow the parent to feel more involved with the study in order to benefit participant retention
- [ ] To capture shared genetic information and environmental/contextual factors associated with mental health outcomes

<details>
<summary>Click to see answer</summary>

- Parents may be able to report about certain domains such as externalizing symptoms more accurately than the child
- Parents have greater access to knowledge of family history
- Parent mental health may color their reports of the child
- To capture shared genetic information and environmental/contextual factors associated with mental health outcomes

***

</details>

**Question 5**

Which demographic information is collected in order to measure socioeconomic status? (select all that apply)

- [ ] Household income data is objective and thus is used as the sole indicator of socioeconomic status in ABCD 
- [ ] A given income may provide different levels of financial stability in different parts of the country, and thus parental occupation, education, and family structure are also collected
- [ ] Family financial adversity and neighborhood adversity provide additional important insight into an individual’s lived socioeconomic situation
- [ ] Rather than relying on participant report, poverty norms in geographic areas (determined by zip code) are used to estimate a family’s socioeconomic status

<details>
<summary>Click to see answer</summary>

- A given income may provide different levels of financial stability in different parts of the country, and thus parental occupation, education, and family structure are also collected
- Family financial adversity and neighborhood adversity provide additional important insight into an individual’s lived socioeconomic situation

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

For this question you will use the ABCD dataset to explore the relationship between sample size and effect size. If you do not have access to the ABCD data, data have been simulated in the exercises repo.

First, if you have not done so, you will need to download the ABCD dataset. See [here](https://docs.google.com/document/d/1q8Tzm__Ead_oybJxdQdMR-IcvPPdeyFCq1OEXDLb8wk/edit#heading=h.tep60nzg7x89) or [here](https://docs.google.com/document/d/1CRU5y3CGDYsaPv1FBkQhJ8ESTtem70RHQ1Q3AmVdOv0/edit?usp=sharing) for information about how to do this.

Second, in your favorite programming language, read in the data element called “abcd_smrip201.txt”. This file contains structural MRI data. 

Third, subset this file to only include the participant’s sex and volumes of the left and the right hippocampus (‘sex’, 'smri_vol_scs_hpuslh','smri_vol_scs_hpusrh'), then create an new vector that includes sum total volume of both the left and right hippocampi. 

Now you have the total hippocampal volume for both male and female participants. Now we can subset these data at multiple sample sizes to see the relationship between effect size and sample size. Create a vector of sample sizes beginning at 10 and ending at 1000, with increments of 20 (so, 50 different sample sizes). 

For each sample size, loop through a large number of iterations (eg, 1000) of subsetting the full male and female participant data so that each iteration has a subset where the number of male and female participants equals the sample size. For each iteration, calculate the raw effect size, the cohen’s d, and the z-scored cohen’s d. Also make sure to record the sample size for each iteration. Now calculate these values for each sample size with your specified number of iterations. For 1000 iterations over 50 sample sizes, this took ~8 minutes on the jupyterhub.

When you are finished calculating the numbers, plot the results. You’ll need three plots, one for raw effect size, cohen’s d, and z-scored cohen’s d.

According to your results, as sample size increases which of the following are generally true (more or less, there will be variability across iterations).

- Raw effect decreases, cohen’s d increases, z stays the same
- Raw effect increases, cohen’s d stays the same, z decreases
- Raw effect stays the same, cohen's d decreases, z increases

<details>
<summary>Click to see answer</summary>

- Raw effect stays the same, cohen's d decreases, z increases

</details>