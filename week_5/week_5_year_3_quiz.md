# Week 5 Quiz

### Quiz Instructions



### ReproNim FAIR data questions

**Question 6**

Which of the following are true of digital object identifiers (DOIs)? Select all that apply.

- [ ] DOIs are globally unique
- [ ] The object’s URL will never change
- [ ] DOIs are persistent
- [ ] DOIs are resolvable
- [ ] DOIs receive a unique accession number

<details>
<summary>Click to see answer</summary>

- DOIs are globally unique
- DOIs are persistent
- DOIs are resolvable

**Explanation**

The object's URL may change, though it is the responsibility of the object's host to report that the URL has changed so that the **globally unique** DOI can remain **persistent** and  **resolve** to the appropriate URL.

Object hosts (e.g., Openneuro.org) can give objects accession numbers, but these are not associated directly with the DOI and are not guaranteed to be globally unique and/or persistent.

***

</details>

**Question 7**

The [MyConnectome](https://openneuro.org/datasets/ds000031/versions/00001) dataset is a neuroimaging dataset available on openneuro.

Which of the following are globally unique and persistent identifiers that point to this dataset? Select all that apply.

- [ ] https://openneuro.org/datasets/ds000031/versions/00001
- [ ] ds000031
- [ ] 10.18112/P2159B
- [ ] 0000-0001-6755-0259
- [ ] 10.1016/j.neuron.2015.06.037
- [ ] https://doi.org/10.18112/P2159B

<details>
<summary>Click to see answer</summary>

- 10.18112/P2159B
- https://doi.org/10.18112/P2159B

**Explanation**

- https://openneuro.org/datasets/ds000031/versions/00001 is the object's current URL, though this is not the DOI
- ds000031 is the accession number assigned by Openneuro.org, not the DOI
- 0000-0001-6755-0259 is the ORCID of one of the authors, not the dataset
- 10.1016/j.neuron.2015.06.037 is a DOI, but it is the DOI of the dataset publication, not the dataset itself

***

</details>

**Question 8**

 Which license allows users to freely distribute the materials as long as attribution is given?

- CC-0
- CC-BY
- CC-NC
- CC-INFC

<details>
<summary>Click to see answer</summary>

CC-BY

Source: [Creative Commons: CC-BY](https://creativecommons.org/licenses/by/4.0/)

***

</details>

For the next questions, you’ll need the following sample dataset repository: https://github.com/ABCD-ReproNim/sample_dataset

To get set up, complete the following steps:

1. Fork the sample dataset repository to create your own copy.
2. Clone your forked version of this repository onto your local machine.

***

**Question 9**

Which statement is true regarding the information about the dataset that the `README.md` and the `dataset_description.json` files contain?

- `README.md` contains structured metadata, `dataset_description.json` contains unstructured metadata
- `README.md` contains structured metadata, `dataset_description.json` contains structured metadata
- `README.md` contains unstructured metadata, `dataset_description.json` contains structured metadata
- `README.md` contains unstructured metadata, `dataset_description.json` contains unstructured metadata

<details>
<summary>Click to see answer</summary>

`README.md` contains unstructured metadata, `dataset_description.json` contains structured metadata

***

</details>

**Question 10**

Using Python or R, read the following tab-separated files into memory: `phenotype/pheno1.tsv` and `phenotype/pheno2.tsv`, then examine the contents of these data frames.

Select all statements that apply to these files:

- [ ] Both files are individually machine readable
- [ ] Both are individually human readable
- [ ] Humans could accurately integrate data across both files without additional information
- [ ] Machines could accurately integrate data across both files without additional information

<details>
<summary>Click to see answer</summary>

- Both files are individually machine readable
- Both are individually human readable
- Humans could accurately integrate data across both files without additional information

**Explanation**

The `handedness` column in these two files are encoded differently. One file uses "left" and "right", whereas the other uses "L" and "R". While humans could reason and integrate between files, a computer would not inherently know that "L" = "left" and "R" = "right" without further information.

Hint: If you need to work with non-curated categorical data like this, you might consider using libraries like [dirty_cat](https://dirty-cat.github.io/stable/) in Python.

***

</details>
