# Week 12 Quiz

### Quiz Instructions

In this Week 12 Quiz, we will ask you a few questions about [Longitudinal Models
and Machine Learning](https://abcd-repronim.github.io/materials/week-12/).

***

## Longitudinal modeling questions

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

## Machine learning questions

In this quiz, we're going to explore some of the concepts presented in the machine learning lecture. First, let’s fetch a pre-written Jupyter Notebook with example code to guide you through the assignment. This notebook is meant as a fully executable guide that you can copy and paste code blocks from as you complete the questions we ask you below.

$ wget https://raw.githubusercontent.com/ABCD-ReproNim/exercises/main/week_12/machine_learning.md

You can open `machine_learning.md` on the JupyterHub as a Notebook by right clicking the file then choosing "Open With" and "Notebook".

**Question 6**

The corresponding section of the Jupyter notebook presents two options for pipeline ordering: (A) data imputation before splitting and (B) data splitting before imputation. Based on the lecture and your understanding of the Jupyter notebook, which of the two orderings is correct and why?

- [ ] Option A because it achieves a higher accuracy score.
- [ ] Option B because it achieves a lower accuracy score and one should report the more pessimistic score to avoid overfitting.
- [ ] Option A because the data is split after imputation and immediately before model fitting, therefore the imputation is the same for the entire dataset.
- [ ] Option B because the data is imputed before splitting, thereby preventing leakage of information between the training and test sets.

<details>
<summary>Click to see answer</summary>

- [ ] Option A because it achieves a higher accuracy score.
  - The downstream model performance is not a factor in determining the correct order.
- [ ] Option B because it achieves a lower accuracy score and one should report the more pessimistic score to avoid overfitting.
  - It makes sense that the accuracy for option A is higher since the imputed values in the test set have "seen" information from the training set. However, this has more to do with the concept of leakage, not overfitting. Moreover, the choice of option B would be correct even if it resulted in improved accuracy. In fact, if you experiment with different random seeds, you may indeed find one for which option B improves model performance.
- [ ] Option A because the data is split after imputation and immediately before model fitting, therefore the imputation is the same for the entire dataset.
  - This option allows leakage of information between the train and test sets. The imputed values in the test set have "seen" information from the training set.
- [x] Option B because the data is imputed before splitting, thereby preventing leakage of information between the training and test sets.
  - This is the correct answer. Think of the imputation strategy as part of the model. It should be validated along with the `SVC` estimator.

***

</details>

**Question 7**

Based on the plot you generated for this question in the Jupyter notebook, which of the following statements is true?
(select all that apply)

- [ ] Increasing the sample size narrowed the distribution of test accuracies.
- [ ] Increasing the sample size had no effect on the distribution of test accuracies.
- [ ] By chance, some test splits for the smallest two sample sizes yielded accuracies that outperformed all test splits from the three highest sample sizes.
- [ ] The test accuracy distributions for small sample sizes supports the practice of using a single train/test split (i.e. one of the dots) to evaluate model performance, rather than the more computationally expensive cross-validation.

<details>
<summary>Click to see answer</summary>

- [x] Increasing the sample size narrowed the distribution of test accuracies.
  - Correct. As also noted in the lecture, large sample sizes yield tighter distributions of test error.
- [ ] Increasing the sample size had no effect on the distribution of test accuracies.
  - Incorrect. See above.
- [x] By chance, some test splits for the smallest two sample sizes yielded accuracies that outperformed all test splits from the three highest sample sizes.
  - This is a direct consequence of the points above. With wider test error distributions for small sample sizes, by chance, some test splits will yield dramatically better results from the tails of the wider distributions.
- [ ] The test accuracy distributions for small sample sizes supports the practice of using a single train/test split (i.e. one of the dots) to evaluate model performance, rather than the more computationally expensive cross-validation.
  - Quite the opposite. Because of the point directly above, it is crucial to evaluate model performance on more than just a single train/test split.

***

</details>

**Question 8**

In the corresponding section of the Jupyter notebook, you re-executed an example from the nilearn library that compared different classifiers on a visual object recognition decoding task. Take a look at the plot you generated. Now suppose we are researchers focused exclusively on predicting chair recognition in this dataset? Which estimator
gave us the best accuracy for chair recognition?

- [ ] `svc_l2`
- [ ] `svc_l1`
- [ ] `logistic_l1`
- [ ] `logistic_l2`
- [ ] `ridge_classifier`

<details>
<summary>Click to see answer</summary>

`svc_l1` gave the best performance. However, qualify this result with your understanding of test error distributions from the previous
question.

***

</details>

**Question 9**

(True/False) Based on the lecture, because we tested all of these estimators with cross-validation before picking the best one, we have a reliable estimation of the `svc_l1` model performance.

- True
- False

<details>
<summary>Click to see answer</summary>

- False. We used test set results (through cross-validation) to select the best model, thereby fitting the "model-choice" parameter to the test sets. Not that we've used all of our data, how then should we test that model choice?

***

</details>

**Question 10**

Based on the plot that you generated in the last part of the Jupyter notebook, you should choose the complex tree model if your objective is to memorize the training data (both its signal and its noise). Which model should you use if your objective is to generalize to new, unseen data?

- Simple tree model
- Complex tree model
- Ensemble of simple tree models
- Ensemble of complex tree models

<details>
<summary>Click to see answer</summary>

- The simple tree ensemble generalizes to unseen data better than both the complex and simple individual decision trees. The example notebook does not test a complex tree ensemble, but you should try it out. How does an ensemble of complex trees compare to the ensemble of simple trees?

```python
regr_4 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=15), n_estimators=300, random_state=rng)
```

***

</details>
