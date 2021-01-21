# Week 8 Quiz

### Quiz Instructions

In this Week 8 Quiz, we will ask you a few questions about the ABCD Culture and Environment Assessments and Data Versioning and Transformation with DataLad.

***

## ABCD questions

**Question 1**

Which general parameters were considered when deciding which culture and environment factors to include in the ABCD Study (select all that apply)?

- [ ] Being a component in the PhenX toolkit
- [ ] Time to administer
- [ ] Validity across cultures
- [ ] Racial and ethnic group classifications that align with census groups

<details>
<summary>Click to see answer</summary>

- Being a component in the PhenX toolkit
- Time to administer
- Validity across cultures

The Zucker et al paper specifically mentions that the census group classifications are inadequate.

***

</details>

**Question 2**

The ABCD Study aimed to recruit a certain percentage of participants from a "high risk" group, where high risk is identified as a likelihood to use marijuana by age 14-15 and measured using a screening developed by Loeber et al, 2018. What was the recruitment goal for this "high risk" group?

- 40%
- 45%
- 50%
- 55%
- 60%


<details>
<summary>Click to see answer</summary>

- 50%

***

</details>

**Question 3**

The Culture and Environment component of the ABCD protocol has a modest ability to differentiate between these higher and lower risk groups. For the baseline data, 64% of the tests of difference between the higher and lower risk groups are significant. How many of these tests make the 0.20 cut-off for a meaningful effect size?

- None
- 2
- 4
- 7


<details>
<summary>Click to see answer</summary>

- 4

This can be answered by looking at Figure 4 of the Zucker et al. paper or simply by reading its conclusion.

***

</details>

**Question 4**

With one exception, in the Culture and Environment component of the ABCD Study, the baseline parent and youth reports all show the same patterns with the regard to sex differences. For which measure was the sex difference (or lack thereof) found in the youth report not found in the parent report?

- Neighborhood Safety
- FES Conflict subscale
- SDQ Prosocial Behavior
- Parental Monitoring

<details>
<summary>Click to see answer</summary>

- Neighborhood Safety

Youth reported no sex difference in neighborhood safety, while parents reported that daughters have a lesser sense of safety in their neighborhoods than do their sons.

***

</details>

**Question 5**

Which of the following measures were administered for the first time at the one-year follow-up assessment for youth (select all that apply)?

- [ ] PhenX Neighborhood Safety/Crime
- [ ] Perceived Discrimination Scale
- [ ] Prosocial Tendencies
- [ ] Family Environment Scale (family conflict subscale) Wills Problem Solving

<details>
<summary>Click to see answer</summary>

- Perceived Discrimination Scale
- Prosocial Tendencies

***

</details>

## ReproNim questions

The following questions focus on using DataLad. A summary of the DataLad commands presented in the [Week 8 ReproNim lecture](https://youtu.be/udLVUyZQanw) can be found [here](http://handbook.datalad.org/en/latest/code_from_chapters/ABCD.html#abcd).

**Question 6**

Choose all statements that are true about git and git-annex.


- [ ] Files given to git-annex are write-protected and need to be unlocked before modifications can be made.
- [ ] Content cloned using either git or git-annex is immediately available.
- [ ] You can configure what content is annexed by git-annex in the .gitattributes file of your dataset.
- [ ] Only metadata of the content that is cloned using git-annex is immediately available.


<details>
<summary>Click to see answer</summary>

- Files given to git-annex are write-protected and need to be unlocked before modifications can be made.
- You can configure what content is annexed by git-annex in the .gitattributes file of your dataset.
- Only metadata of the content that is cloned using git-annex is immediately available.

***

</details>

**Question 7**

Navigate to your home directory on the Jupyter Hub. First, create a DataLad dataset using the YODA configuration. Let’s call this dataset directory `week8_analysis`. Next, clone the structural portion of the Study Forrest dataset (https://github.com/psychoinformatics-de/studyforrest-data-structural) as a subdataset named ‘data’. What is the current size of the ‘data’ directory?

Note: in the DataLad lecture, Dr. Wagner uses a command to clone a dataset hosted on GitHub by specifying its location with `git@github.com:[remote repository path]`. This `git@` way of specifying a dataset location requires ssh-based access, and if you haven't already set up an RSA key on the JupyterHub you may run into an error. However, you can also specify a dataset location simply by inputting a url into the `datalad clone` command, which does not require setting up RSA credentials. If you need more information on argument options for the `datalad clone` command you can always type `datalad clone --help`.

- 1.2 MB
- 1.8 MB
- 2.3 MB
- 2.5 MB


<details>
<summary>Click to see answer</summary>

- 1.8 MB

see code in `exercises/week_8` for a solution (coming soon!)

***

</details>

**Question 8**

Let's get only the T1w file content stored in the `anat` subdirectories of the dataset we cloned. What command would you use (assuming you’re currently in the top level of the data directory)?

- `datalad get anat/T1w`
- `datalad get sub-*/anat/*T1w*`
- `datalad get T1w`
- `datalad get sub-*/anat/*`

<details>
<summary>Click to see answer</summary>

- `datalad get sub-*/anat/*T1w*`

***

</details>

**Question 9**

We notice that this dataset is missing a `dataset_description.json` file rendering it not a fully BIDS compliant dataset (and this would pose a problem for running BIDS pipelines). Create this file with the following content in it: {"Name": "Example dataset", "BIDSVersion": "1.0.2"}. (Note: If you’d like to know more about BIDS dataset_description.json files and what goes into them you can find more information here.) To make Datalad aware of this addition, which would you run?

- `git add dataset_description.json`
- `git commit -m “added a dataset description file”`
- `datalad save -m “added a dataset description file” dataset_description.json`

<details>
<summary>Click to see answer</summary>

- `datalad save -m “added a dataset description file” dataset_description.json`

***

</details>

**Question 10**

Working with BIDS compliant datasets allows us to easily launch various pipelines and create BIDS compliant derivatives (e.g., standardized, machine-readable outputs from processing pipelines). The proper way of storing such derivatives is detailed [here](https://bids-specification.readthedocs.io/en/latest/02-common-principles.html#storage-of-derived-datasets). Using the `datalad-containers` extension, we can launch [MRIQC](https://mriqc.readthedocs.io/en/latest/) and generate image quality metrics for structural MRI scans. ReproNim has made a ton of popular neuroimaging pipelines available to install as a Datalad dataset (https://github.com/ReproNim/containers), and the link has more information on how to use this dataset in conjunction with `datalad-containers`.  You may also find it helpful to review the commands covered in the [containers section](http://handbook.datalad.org/en/latest/code_from_chapters/ABCD.html#computational-reproducibility) of this week’s [DataLad lecture](https://youtu.be/udLVUyZQanw?t=1962).

Step 1: Based on the 1st protocol outlined in the above linked [derivative storage guide](https://bids-specification.readthedocs.io/en/latest/02-common-principles.html#storage-of-derived-datasets), create a `derivatives` directory at the root of (i.e., at the same level of) `data` and a separate directory called `mriqc` within the `derivatives` directory.

Step 2: At the root of your `week8_analysis` directory, install the aforementioned ReproNim Datalad dataset using: `datalad install -d . ///repronim/containers`

Step 3: BIDS pipelines require a work directory, and it is preferable for it to be ignored by Git. From the root directory, run the following: `echo "workdir/" > .gitignore && datalad save -m "Ignore workdir" .gitignore`

Step 4: Use `datalad containers-run` to run MRIQC on sub-01’s T1w data and output the results to the `mriqc` directory we just created. Hint: This will require specifying a path to a container (see [here](https://github.com/ReproNim/containers#a-typical-workflow) for an example of how to specify the container and other arguments of interest), the input path, output path, the participant of interest, the modality of interest, and the work directory to be used. If you need help with using the `datalad containers-run` command you can always type `datalad containers-run --help`. The [MRIQC documentation](https://mriqc.readthedocs.io/en/latest/) also provides additional information on how to specify MRIQC specific arguments.

Assuming these steps were executed successfully, you should now be able to access the following filepath from the `mriqc` directory: `sub-01/anat/sub-01_T1w.json`. This JSON file contains a variety of different image quality metrics; you can find the abbreviations and explanations here. What is the contrast to noise ratio for sub-01’s T1w scan?


- 0.343
- 4.344
- 3.811
- 1.119

<details>
<summary>Click to see answer</summary>

- 3.811

see code in `exercises/week_8` for a solution (coming soon!)

</details>
