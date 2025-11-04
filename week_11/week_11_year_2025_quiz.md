# Week 11 Quiz

### Quiz Instructions
In this Week 12 Data Exercise, we will ask you a few questions about [Biospecimens in ABCD and Machine Learning](https://abcd-repronim.github.io/materials/week-11/).

***

## ABCD questions

**Question 1**

What biospecimens are collected at multiple timepoints in the ABCD Study? (select all that apply)

- [ ] Breath, urine, and saliva to detect recent substance use
- [ ] Saliva to measure pubertal hormones
- [ ] Blood and saliva for DNA analysis
- [ ] Hair to detect substance use
- [ ] Baby teeth to estimate environmental exposure

<details>
<summary>Click to see answer</summary>

- Breath, urine, and saliva to detect recent substance use
- Saliva to measure pubertal hormones
- Hair to detect substance use

***

</details>

**Question 2**

What are some methodological considerations for dealing with biospecimen data? (select all that apply)

- [ ] Who is missing from the dataset and why? Is there a sampling bias for who opts in (or out) of providing certain biospecimens?
- [ ] Are the details of specimen collection (e.g., time of day) accurately recorded or labeled? How to identify and deal with potential errors and inconsistencies?
- [ ] How to perform quality checks, determine final sample selection, and any additional decisions that increase experimenter degrees of freedom?
- [ ] What confounds may be explaining variance in the data (e.g. caffeine, physical activity)?

<details>
<summary>Click to see answer</summary>

- Who is missing from the dataset and why? Is there a sampling bias for who opts in (or out) of providing certain biospecimens?
- Are the details of specimen collection (e.g., time of day) accurately recorded or labeled? How to identify and deal with potential errors and inconsistencies?
- How to perform quality checks, determine final sample selection, and any additional decisions that increase experimenter degrees of freedom?
- What confounds may be explaining variance in the data (e.g. caffeine, physical activity)?

***

</details>

**Question 3**

Individual differences in pubertal hormone levels, patterns, and sensitivity can contribute to differences in brain and body maturation, mental health, substance use, and behavioral problems.

- True
- False

<details>
<summary>Click to see answer</summary>

- True

***

</details>

**Question 4**

Baby teeth provide layer-by-layer information about environmental exposure beginning in the second trimester of pregnancy

- True
- False

<details>
<summary>Click to see answer</summary>

- True

***

</details>

**Question 5**

What are some recommendations for dealing with biospecimen data? (select all that apply)

- [ ] Visualize data to identify physiologically improbable values
- [ ] Publish experimenter decision trees and scripts for transparency and reproducibility
- [ ] Trust that the data are accurate even if some data points seem unlikely
- [ ] Be informed by approaches and effect sizes reported in the literature
- [ ] Consider sociodemographic factors, sample bias, and methods

<details>
<summary>Click to see answer</summary>

- Visualize data to identify physiologically improbable values
- Publish experimenter decision trees and scripts for transparency and reproducibility
- Be informed by approaches and effect sizes reported in the literature
- Consider sociodemographic factors, sample bias, and methods

***

</details>

## Machine learning questions

In this quiz, we're going to explore some of the concepts presented in the machine learning lecture. First, let’s fetch a [pre-written Jupyter Notebook](https://github.com/ABCD-ReproNim/exercises/blob/main/week_12/machine_learning.md) with example code to guide you through the assignment. This notebook is meant as a fully executable guide that you can copy and paste code blocks from as you complete the questions we ask you below.

`$ wget https://raw.githubusercontent.com/ABCD-ReproNim/exercises/main/week_12/machine_learning.md`

You can open `machine_learning.md` on the JupyterHub as a Notebook by right clicking the file then choosing **Open With** and **Notebook**.

**Question 6**

The corresponding section of the Jupyter notebook presents two options for pipeline ordering: (A) data imputation before splitting and (B) data splitting before imputation. Based on the lecture and your understanding of the Jupyter notebook, which of the two orderings is correct and why?

- [ ] Option A because it achieves a higher accuracy score.
- [ ] Option B because it achieves a lower accuracy score and one should report the more pessimistic score to avoid overfitting.
- [ ] Option A because the data is split after imputation and immediately before model fitting, therefore the imputation is the same for the entire dataset.
- [ ] Option B because the data is imputed after splitting, thereby preventing leakage of information between the training and test sets.

<details>
<summary>Click to see answer</summary>

- [ ] Option A because it achieves a higher accuracy score.
  - The downstream model performance is not a factor in determining the correct order.
- [ ] Option B because it achieves a lower accuracy score and one should report the more pessimistic score to avoid overfitting.
  - It makes sense that the accuracy for option A is higher since the imputed values in the test set have "seen" information from the training set. However, this has more to do with the concept of leakage, not overfitting. Moreover, the choice of option B would be correct even if it resulted in improved accuracy. In fact, if you experiment with different random seeds, you may indeed find one for which option B improves model performance.
- [ ] Option A because the data is split after imputation and immediately before model fitting, therefore the imputation is the same for the entire dataset.
  - This option allows leakage of information between the train and test sets. The imputed values in the test set have "seen" information from the training set.
- [x] Option B because the data is imputed after splitting, thereby preventing leakage of information between the training and test sets.
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

- [x] `svc_l1`
  - However, qualify this result with your understanding of test error distributions from the previous question.

***

</details>

**Question 9**

(True/False) Based on the lecture, because we tested all of these estimators with cross-validation before picking the best one, we have a reliable estimation of the `svc_l1` model performance.

- [ ] True
- [ ] False

<details>
<summary>Click to see answer</summary>

- [x] False
  - We used test set results (through cross-validation) to select the best model, thereby fitting the "model-choice" parameter to the test sets. Not that we've used all of our data, how then should we test that model choice?

***

</details>

**Question 10**

Based on the plot that you generated in the last part of the Jupyter notebook, you should choose the complex tree model if your objective is to memorize the training data (both its signal and its noise). Which model should you use if your objective is to generalize to new, unseen data?

- [ ] Simple tree model
- [ ] Complex tree model
- [ ] Ensemble of simple tree models
- [ ] Ensemble of complex tree models

<details>
<summary>Click to see answer</summary>

- [x] Ensemble of simple tree models
  - The simple tree ensemble generalizes to unseen data better than both the complex and simple individual decision trees. The example notebook does not test a complex tree ensemble, but you should try it out. How does an ensemble of complex trees compare to the ensemble of simple trees?

```python
regr_4 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=15), n_estimators=300, random_state=rng)
```

***

</details>
