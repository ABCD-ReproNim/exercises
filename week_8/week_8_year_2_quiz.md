# Week 8 Quiz

### Quiz Instructions

In this Week 8 Quiz, we will ask you a few questions about the [ABCD Linked External Data]([https://[https://www.youtube.com/watch?v=fnY_As9b7Uw]) and [Data Versioning and Transformation with DataLad](https://youtu.be/udLVUyZQanw).

***

## ABCD questions

**Question 1**

Which statement best defines “place-based health”?

- Health is determined only by genetics
- Health is shaped mainly by hospital quality
- Health is shaped by where people live, work, and play
- Health is unaffected by geography

<details>
<summary>Click to see answer</summary>

- Health is shaped by where people live, work, and play

***

</details>

**Question 2**

In ABCD Linked External Data (LED), which addresses are used for environmental linkages?

- Current address only
- Baseline addresses (ages 9–10)
- All lifetime addresses
- School addresses only


<details>
<summary>Click to see answer</summary>

-  Baseline addresses (ages 9–10)

***

</details>

**Question 3**

Can ABCD share residential histories (addresses) with data users?

- No; addresses are PII, so geocoding is performed within ABCD’s secure environment
- Yes; but only for longitudinal researchers
- Yes; they are public records
- No; but de-identified full geocodes are emailed on request


<details>
<summary>Click to see answer</summary>

- No; addresses are PII, so geocoding is performed within ABCD’s secure environment


***

</details>

**Question 4**

What changed for LED in the 6.0 release?

- New data and new names
- No new data; variable names/descriptions changed and warnings added
- No changes at all
- All variables were removed

<details>
<summary>Click to see answer</summary>

- No new data; variable names/descriptions changed and warnings added

***

</details>

**Question 5**

Which statement best describes the Adolescent Neural Urbanome?

- A genetic database of ABCD participants
- A repository of household sensor data capturing micro-environments indoors
- A neuroimaging atlas that maps adolescent brain networks across scanners only
- A framework organizing environmental LED variable sets to contextualize where ABCD youth lived at baseline and inform policy

<details>
<summary>Click to see answer</summary>

- A framework organizing environmental LED variable sets to contextualize where ABCD youth lived at baseline and inform policy

***

</details>

## ReproNim questions

For students who have active DUCs, We recommend you use the online version of
the [ABCD-ReproNim Jupyterhub](https://abcd.repronim.org/) (read more on how to use the JupyterHub [here](https://docs.google.com/document/d/1kXvK2c_N9TkIAYn21WfzlCPtJvxhjW13Ftf0DwnAnlg/edit#heading=h.yb1hc7y3vc15) and request access [here](https://docs.google.com/forms/d/e/1FAIpQLSefrxRzdjFak_BoxTL5bE-TnsJdg9KbGvFdOwuW7zliZ96z7g/viewform?usp=sf_link)), in which [DataLad](https://www.datalad.org/) is already installed. You can also use a [local version of the ABCD-ReproNim JupyterHub container](https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439). Alternatively, you can work with a local, non-JupyterHub instance of DataLad by following the installation instructions [here](https://handbook.datalad.org/en/latest/intro/installation.html).

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

Navigate to your home directory on the Jupyter Hub. First, create a DataLad dataset using the YODA configuration. Let’s call this dataset directory `week8_analysis`. Next, clone the structural portion of the [Study Forrest dataset](https://github.com/psychoinformatics-de/studyforrest-data-structural) as a subdataset named `data`. What is the current size of the `data` directory?

Note: in the DataLad lecture, Dr. Wagner uses a command to clone a dataset hosted on GitHub by specifying its location with `git@github.com:[remote repository path]`. This `git@` way of specifying a dataset location requires ssh-based access, and if you haven't already set up an RSA key on the JupyterHub you may run into an error. However, you can also specify a dataset location simply by inputting a url into the `datalad clone` command, which does not require setting up RSA credentials. If you need more information on argument options for the `datalad clone` command you can always type `datalad clone --help`.

- 200 KB
- 872 KB
- 1.9 MB
- 2.5 MB


<details>
<summary>Click to see answer</summary>

- 872 KB (if using the local docker)
- 1.9 M (if using JupyterHub)

Datalad solution
- `datalad create -c yoda week8_analysis`
- `cd week8_analysis`
- `datalad clone -d . https://github.com/psychoinformatics-de/studyforrest-data-structural.git data/`
- `cd data`
- `du -sh`

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

We notice that the `dataset_description.json` file in this dataset is missing `BIDSVersion`, rendering it not a fully BIDS compliant dataset (and this would pose a problem for running BIDS pipelines). Assuming you have updated this content as `BIDSVersion": "1.0.2"` (Note: If you’d like to know more about BIDS `dataset_description.json` files and what goes into them you can find more information [here](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html).), to make DataLad aware of this addition, which would you run?

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

Step 1: Based on the 1st protocol outlined in the above linked [derivative storage guide](https://bids-specification.readthedocs.io/en/latest/02-common-principles.html#storage-of-derived-datasets), create 1) a `derivatives` directory within the `data` directory and 2) another directory called `mriqc` within the `derivatives` directory. Save the change `datalad save -m "adding new folders"` 

Step 2: At the root of your `week8_analysis` directory, install the aforementioned ReproNim Datalad dataset using: `datalad install -d . ///repronim/containers`

Step 3: BIDS pipelines require a work directory, and it is preferable for it to be ignored by Git. From the root directory, run the following: `echo "workdir/" > .gitignore && datalad save -m "Ignore workdir" .gitignore`

Step 4: If you have not downloaded the content in all `anat` folders, run the following `datalad get data/sub-*/anat/*`

Step 5: Use `datalad containers-run` to run MRIQC on sub-01’s T1w data and output the results to the `mriqc` directory we just created. Hint: This will require specifying a path to a container (see [here](https://github.com/ReproNim/containers#a-typical-workflow) for an example of how to specify the container and other arguments of interest), the input path, output path, the participant of interest, the modality of interest, and the work directory to be used. If you need help with using the `datalad containers-run` command you can always type `datalad containers-run --help`. The [MRIQC documentation](https://mriqc.readthedocs.io/en/latest/running.html) also provides additional information on how to specify MRIQC specific arguments.

Assuming these steps were executed successfully, you should now be able to access the following filepath from the `mriqc` directory: `sub-01/anat/sub-01_T1w.json`. This JSON file contains a variety of different image quality metrics; you can find the abbreviations and explanations [here](https://mriqc.readthedocs.io/en/latest/iqms/t1w.html). What is the contrast to noise ratio for sub-01’s T1w scan?


- 0.343
- 4.344
- 3.811
- 1.119

<details>
<summary>Click to see answer</summary>

- 3.811

Datalad solution: 
- `cd /home/jovyan/week8_analysis` (if you are using the local docker, change the path accordingly)
- `mkdir data/derivatives/mriqc -p && datalad save -m "adding new folders"` 
- `datalad install -d . ///repronim/containers`
- `echo "workdir/" > .gitignore && datalad save -m "Ignore workdir" .gitignore`
- `datalad get data/sub-*/anat/*`
- `datalad containers-run -n containers/bids-mriqc --input data/sub-01/anat/sub-01_T1w.nii.gz --output data/derivatives/mriqc data data/derivatives/mriqc participant --participant-label 01 -m T1w -w workdir`

Template for running datalad containers
```
datalad containers-run \
        -n containers/bids-mriqc \
        --input sourcedata \
        --output . \
        '{inputs}' '{outputs}' participant --participant-label %02d -w workdir
```

Note that the --input to Datalad differs from the input argument to mriqc. This is because we're specifying a specific file for Datalad to download as opposed to the root of the BIDS directory that MRIQC expects. The output is the same for both Datalad and MRIQC.

</details>
