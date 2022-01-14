# Week 2 Bonus Quiz on DEAP

Only researchers who have been approved to access ABCD Study data are permitted to access DEAP. This is a bonus quiz for students who have successfully gained access to DEAP. This quiz is not required, but is recommended if you have access to DEAP.

This quiz will be available to you throughout the course. Thus, if you do not currently have access to ABCD data, but your access is approved in the future, then you will be able to complete this quiz at a later date.

**Question 1**

Using the DEAP “Explore” tool, find the scores for the NIH Toolbox Oral Reading Recognition Test Age 3+ v2.0, Age-Corrected Standard Score.

Hint: In the DEAP ABCD Ontology, all of the measures from this test have the prefix “nihtbx_reading.”

What is the mean age-corrected standard score?

- 104.256
- 102.218
- 101.714
- 103.492

**Question 2**

Using the DEAP “Limit” tool, select only study participants who are siblings, twins, or triplets AND who have an age-corrected reading score (see above question for context) greater than 110. How many study participants satisfy those criteria in the baseline data? It may help to examine the other presets to see how to combine selection queries and how to select siblings, twins, or triplets.

- 748
- 689
- 2,274
- 2,886

**Question 3**

Using the DEAP “Analyze” tool, build a GAMM model where the dependent variable is the aforementioned age-adjusted reading score and the independent variable is the average fractional anisotropy within the left inferior longitudinal fasciculus (which goes by the name “dmri_dti.fa_fiber.at_ilf.lh” in the DEAP ontology). Select only right-handed subjects and group by “high.educ.bl”. Use the default fixed effect covariates and select “FAMILY” and “DEVICE” for random effects.

What is the delta-R^2 reported in the effect size table for this model?

- 2.46%
- 2.44%
- 2.50%
- 2.39%
