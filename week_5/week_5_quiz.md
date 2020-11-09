# Week 5 Quiz

### Quiz Instructions

In this Week 5 Quiz, we will ask you a few questions about the ABCD neurocognitive assessments and FAIR data concepts.

***

### ABCD (neurocognitive assessments) Questions

**Question 1**

 What were the overarching motivations for the tasks selected for the neurocognitive battery? Select all that apply.

 - [ ] the tasks maximize sensitivity to development and other emergent factors across a decade of assessment, starting from the ages of 9-10 
 - [ ]  the tasks minimize participant burden 
 - [ ]  the tasks are comparable to those used for other large studies 
 - [ ]  the tasks cover multiple domains
 - [ ]  all the above
 - [ ]  

**Question 2**

This lecture covered the results of Thompson et al, 2019 whereby principal component analysis was applied to 12 neurocognitive assessments. Based on this study, what were the main principal components underlying the different tasks administered to participants at baseline? Select all that apply.

- [ ] Reward 
- [ ] General cognitive ability
- [ ] Executive function
- [ ] Learning and memory

**Question 3**

Which of these tasks are only offered at one timepoint? Select all that apply.

- [ ] Picture Vocabulary
- [ ] Rey Auditory Verbal Learning Test
- [ ] Stanford Mental Arithmetic Response Time Eval
- [ ] Dimensional Change Card Sort

**Question 4**

Which of these are true of the Cash Choice and Delay Discounting tasks? Select all that apply.

- [ ] A strong association has been reported between temporal delay and substance use 
- [ ] Both of these tasks are administered at each timepoint
- [ ] The decision participants make regarding receiving $75 in three days or $115 in three months are developmentally stable 
- [ ] All the above

**Question 5**

- Environmental exposures might change the developmental trajectory
- Alternate forms of tests must be administered to account for potential practice effects
- Overlapping assessments of youngest and oldest subjects
- All the above

### ReproNim FAIR data questions

**Question 6**

Which of the following are true of digital object identifiers (DOIs)? Select all that apply.

- [ ] DOIs are globally unique
- [ ] The object’s URL will never change
- [ ] DOIs are persistent
- [ ] DOIs are resolvable
- [ ] DOIs receive a unique accession number

**Question 7**

The [MyConnectome](https://openneuro.org/datasets/ds000031/versions/00001) dataset is a neuroimaging dataset available on openneuro.

Which of the following is(are) globally unique and persistent identifier(s) that point to this dataset? Select all that apply.

- [ ] https://openneuro.org/datasets/ds000031/versions/00001
- [ ] ds000031
- [ ] 10.18112/P2159B
- [ ] 0000-0001-6755-0259
- [ ] 10.1016/j.neuron.2015.06.037
- [ ] doi.org/10.18112/P2159B

**Question 8**

 Which license allows users to freely distribute the materials as long as attribution is given?

 - CC-0
 - CC-BY
 - CC-NC
 - CC-INFC

***
For the next questions, you’ll need the following sample dataset repository: https://github.com/ABCD-ReproNim/sample_dataset

To get set up, complete the following steps:
1. Fork the sample_repository to create your own copy
2. Clone your forked version of this repository onto your local machine (or on the ABCD-ReproNim JupyterHub)

***

**Question 9**

Which statement is true regarding the information about the dataset that the `README.md` and the `dataset_description.json` files contain?

- `README.md` contains structured metadata, `dataset_description.json` contains unstructured metadata
- `README.md` contains structured metadata, `dataset_description.json` contains structured metadata
- `README.md` contains unstructured metadata, `dataset_description.json` contains structured metadata
- `README.md` contains unstructured metadata, `dataset_description.json` contains unstructured metadata

**Question 10**

Using Python or R, read the following tab-separated files into memory: `phenotype/pheno1.tsv` and `phenotype/pheno2.tsv`, then examine the contents of these data frames.

Select all statements that apply to these files:

- [ ] Both files are individually machine readable
- [ ] Both are individually human readable
- [ ] Humans could accurately integrate data across both files without additional information
- [ ] Machines could accurately integrate data across both files without additional information