# Week 9 Quiz

### Week 9 Data Exercise Instructions

We will being by asking you a few questions about [ABCD Biospecimens
and Reproducible workflows in Repronim](https://abcd-repronim.github.io/materials/week-9/). Please view the [lecture video](https://youtu.be/QcsifMz5_fQ) before completing this quiz.

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

## ReproNim questions

For today's Repronim questions, you will be using (via the command `datalad create week9_analysis`),
cloning (via the command `datalad clone -d . https://github.com/psychoinformatics-de/studyforrest-data-structural.git data`),
and retrieving T1w data (via the command `datalad get data/sub-*/anat/*T1w*`) from
the [Study Forrest dataset](https://github.com/psychoinformatics-de/studyforrest-data-structural) we worked with
during the [DataLad](https://www.datalad.org/) portion of [last week's quiz](https://github.com/ABCD-ReproNim/exercises/blob/main/week_8/week_8_quiz.md#repronim-questions).
We will also be testing different ways of using FSL's [`FIRST`](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST) to compare results.

We recommend you use the online version of the [ABCD-ReproNim Jupyterhub](http://abcd.repronim.org/), in
which DataLad is already installed. The JupyterHub is open to ABCD-ReproNim students who have 
active [NDA Data Use Certification (DUC)](https://docs.google.com/document/d/18hsT2x15bypuXFcfMQb9Ck_YEB7VvY2j4w5hwbV78A4/edit?usp=sharing) to access ABCD Study data. 
To request access please provide us with your GitHub username [here](https://docs.google.com/forms/d/e/1FAIpQLSefrxRzdjFak_BoxTL5bE-TnsJdg9KbGvFdOwuW7zliZ96z7g/viewform?usp=sf_link).
If you do not have an active DUC You can also use a local version of the ABCD-ReproNim JupyterHub container. Instructions on how to set up a local
instance of our JupyterHub can be found [here](https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439). Alternatively,
you can work with a local, non-JupyterHub instance of DataLad by following the DataLad installation instructions [here](https://handbook.datalad.org/en/latest/intro/installation.html).

**Question 6**

If a researcher performs similar analyses on the same data
and gets a similar result, how would we describe the reproducibility of the result?
The result is:

- Re-executable
- Replicable
- Robust
- Generalizable


<details>
<summary>Click to see answer</summary>

- Robust is the correct answer since you ran a similar
  analysis on the original data.
- Re-executable means you ran the original analysis on the
  original data
- Replicable means you ran the original analysis on a 
  similar dataset
- Generalizable means you ran a similar analysis on a
  similar dataset
***

</details>

**Question 7**

You will be installing the [Study Forrest dataset](https://github.com/psychoinformatics-de/studyforrest-data-structural) again as you did
in the [DataLad](https://www.datalad.org/) questions from
the [Week 8 Quiz](https://github.com/ABCD-ReproNim/exercises/blob/main/week_8/week_8_year_2_quiz.md#repronim-questions), but this time inside a new datalad dataset
that we will name `week9_analysis`.
Assuming you are starting from your home directory on
the [ABCD-ReproNim JupyterHub](https://docs.google.com/document/d/1kXvK2c_N9TkIAYn21WfzlCPtJvxhjW13Ftf0DwnAnlg/edit#heading=h.yb1hc7y3vc15)
(i.e., `/home/jovyan`), reorder the below commands to create the necessary datalad datasets for analysis (note: not all of the commands listed are necessarily needed).
We want a dataset named `data` for our raw data, a dataset named `derivatives` for our results,
T1w images from the first three participants, and an FSL container for the software we will run.

- `cd week9_analysis`
- `datalad create week9_analysis`
- `datalad clone week9_analysis`
- `datalad create -d . derivatives`
- `datalad -d . create https://github.com/psychoinformatics-de/studyforrest-data-structural.git data`
- `datalad clone -d . https://github.com/psychoinformatics-de/studyforrest-data-structural.git data`
- `datalad clone -d derivatives`
- `datalad get data/sub-*/anat/sub-0{1..3}_T1w.nii.gz`
- `datalad containers-add fsl --url https://osf.io/epnxs/download --call-fmt "singularity exec --cleanenv {img} {cmd}"`


## NOTE
If you get an error about running out of disk space when
running the `containers-add` command try changing where singularity builds the image:
```
mkdir ${HOME}/.singularity/build
export SINGULARITY_TMPDIR=$HOME/.singularity/build
```
<details>
<summary>Click to see answer</summary>

- `datalad create week9_analysis`
- `cd week9_analysis`

These two commands must be in this order
- `datalad clone -d . https://github.com/psychoinformatics-de/studyforrest-data-structural.git data`
- `datalad get data/sub-*/anat/sub-0{1..3}_T1w.nii.gz`

These two can happen in any order
- `datalad create -d . derivatives`
- `datalad containers-add fsl --url https://osf.io/epnxs/download --call-fmt "singularity exec --cleanenv {img} {cmd}"`

Cannot clone derivatives or week9_analysis
- `datalad clone -d derivatives`
- `datalad clone week9_analysis`

Cannot `create` an existing repository
- `datalad -d . create https://github.com/psychoinformatics-de/studyforrest-data-structural.git data`

***

</details>

**Question 8**

Next, we are going to determine hippocampal volume from the Study Forrest dataset
using [`FIRST`](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST) (FMRIB’s Integrated Registration and Segmentation Tool).
Additionally, we want to measure the robustness of our analysis by changing a parameter in our
call to `FIRST`.
Specifically, we will be using the command `run_first_all` and we
will vary the parameter `-m` (method) between `fast` and `none` to identify if
the advanced tissue boundary search algorithm impacts our results.
Let's try to unscramble the below command into the correct order as to get the volume of the Left and Right hippocampi.

- `run_first_all containers-run -s datalad --explicit fsl -o data/sub-01/anat/sub-01_T1w.nii.gz --output derivatives/first/sub-01/ -i L_Hipp,R_Hipp -n data/sub-01/anat/sub-01_T1w.nii.gz --input derivatives/first/sub-01/none -m none `

Once you've unscrambled and successfully ran this command replace all instances of `none`
with `fast`.

After both commands successfully finish, you will see two files in your `data` directory
(under a specific participant folder, `sub-01/anat`)
with the suffixes/extensions `*T1w_to_std_sub.mat` and `*T1w_to_std_sub.nii.gz`.
You will need to move these to the `derivatives` folder to ensure you do not modify the
raw dataset.

Check `datalad status` to see what files have been modified/created (assuming you
are in the `week9_analysis` directory).
You may not get very helpful information, so first `cd` into the `data` directory
and type `datalad status` again.
If you copied the files over, the `data` dataset _should_ be clean.
Next, `cd` into the derivatives dataset.
Now you should see all the new files that were created.
Type `datalad save -m "run FIRST on sub-01 with none and fast parameters"`.
`datalad save` will save the changes to the files.

If you have the time, you can run `sub-02` in the same way.

## NOTE
You may get this error in your output:
```
[INFO   ] == Command start (output follows) ===== 
Error: cannot find image data/sub-01/anat/sub-01_T1w.nii.gz
```
If this is the case, you may need to unlock `data/sub-01/anat/sub-01_T1w.nii.gz` via (`datalad unlock data/sub-01/anat/sub-01_T1w.nii.gz`).
and add [`--explicit`](http://docs.datalad.org/projects/container/en/latest/generated/man/datalad-containers-run.html#explicit) to the datalad command.

Unlocking a file means replacing the [`symbolic link`](https://en.wikipedia.org/wiki/Symbolic_link) of the file with a copy
of the file stored in `git-annex`.
By replacing the symbolic link with an actual copy of the file, the software within the container can read an actual file instead of a symbolic link, which some software does not interpret correctly, as is the case here.


<details>
<summary>Click to see answer</summary>

## None
- `datalad containers-run -n fsl --explicit --input data/sub-01/anat/sub-01_T1w.nii.gz --output derivatives/first/sub-01/ run_first_all -i data/sub-01/anat/sub-01_T1w.nii.gz -o derivatives/first/sub-01/none -m none -s L_Hipp,R_Hipp`

## Fast
- `datalad containers-run -n fsl --explicit --input data/sub-01/anat/sub-01_T1w.nii.gz --output derivatives/first/sub-01/ run_first_all -i data/sub-01/anat/sub-01_T1w.nii.gz -o derivatives/first/sub-01/fast -m fast -s L_Hipp,R_Hipp`
***

</details>

**Question 9**

After the container runs FIRST using both methods, we want to compare
the methods.
Load the relevant data (i.e., `_firstseg.nii.gz`) into your
favorite programming language, create a script to extract the volumes
and save them in a table. Place this script in `derivatives/first/code`.

Here is how a python script could look (fill in the blanks):
```
import nibabel as nib
import pandas as pd
from glob import glob
data_dict = {"participant": [], "parameter": [], "volume": []}

# fill in the underscores with the appropriate names
for _______ in glob('../sub-*'):
    _______ = _______.split('/')[-1]
    for _________ in ["none", "fast"]:
        img = nib.load(f'../{participant}/{parameter}_all_{parameter}_firstseg.nii.gz')
        volume = img.get_fdata().astype(bool).sum()

        # update dictionary
        data_dict["participant"].append(_________)
        data_dict["parameter"].append(_________)
        data_dict["volume"].append(_________)

volume_df = pd.DataFrame.from_dict(_____)

volume_df.to_csv('../hippocampal_volume.tsv', sep="\t", index=False)
```
## Bonus

How would you add and run this script using datalad? While inside the `code` directory, use
datalad run python ./analysis.py


<details>
<summary>Click to see answer</summary>

```
import nibabel as nib
import pandas as pd
from glob import glob
data_dict = {"participant": [], "parameter": [], "volume": []}

for participant in glob('../sub-*'):
    participant = participant.split("/")[-1]
    for parameter in ["none", "fast"]:
        img = nib.load(f'../{participant}/{parameter}_all_{parameter}_firstseg.nii.gz')
        # binarize and sum the image
        volume = img.get_fdata().astype(bool).sum()

        # update dictionary
        data_dict["participant"].append(participant)
        data_dict["parameter"].append(parameter)
        data_dict["volume"].append(volume)

volume_df = pd.DataFrame.from_dict(data_dict)

volume_df.to_csv('../hippocampal_volume.tsv', sep="\t", index=False)
```

</details>

**Question 10**

Approximately how large are the volume differences between `none` and `fast`?
Would you consider the result to be robust across our choices of parameters?

- 1's
- 10's
- 100's
- 1000's

<details>
<summary>Click to see answer</summary>

- 100's, I would not consider our result to be robust across our choices of parameters.

</details>
