# Week 7 Quiz

### Quiz Instructions

In this Week 9 Quiz, we will ask you a few questions about the ABCD Biospecimens
and Reproducible workflows in Repronim.

***

## ABCD questions

**Question 1**


<details>
<summary>Click to see answer</summary>

***

</details>

**Question 2**


<details>
<summary>Click to see answer</summary>

***

</details>

**Question 3**


<details>
<summary>Click to see answer</summary>

***

</details>

**Question 4**

<details>
<summary>Click to see answer</summary>

***

</details>

**Question 5**


<details>
<summary>Click to see answer</summary>


***

</details>

## ReproNim questions

For today's Repronim questions, you will be using 
(`datalad create week9_analysis`)
and cloned the studyforrest data (`datalad clone -d . https://github.com/psychoinformatics-de/studyforrest-data-structural.git data`), and retrieved the T1w data `datalad get data/sub-*/anat/*T1w*`
We will be testing different ways of using FSL's FIRST to compare results.

**Question 6**

If a researcher uses performs similar analyses on the same data
and gets a similar result, how would we describe the reproducibility of the result?
The result is:

- Re-executable
- Replicible
- Robust
- Generalizable


<details>
<summary>Click to see answer</summary>

- Robust
***

</details>

**Question 7**

You will be installing with study-forrest dataset again, inside a new datalad dataset
`week9_analysis`.
Assuming you are starting from your home directory (i.e., `/home/jovyan`), Reorder the commands
to create the necessary datalad datasets for analysis.
We want a `data` dataset for our raw data, a `derivatives` dataset for our results,
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

We are going to determine hippocampal volume from the Forrest dataset using [`FIRST`](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST) (FMRIB’s Integrated Registration and Segmentation Tool).
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
You may get this error message `cannot find data/sub-01/anat/sub-01_T1w.nii.gz`,
if this is the case, you may need to unlock `data/sub-01/anat/sub-01_T1w.nii.gz`
and add [`--explicit`](http://docs.datalad.org/projects/container/en/latest/generated/man/datalad-containers-run.html#explicit) to the datalad command.


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

How would you add and run this script using datalad?

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
## BONUS
(while inside the `code` directory)
datalad run python ./analysis.py
***

</details>

**Question 10**
Approximately how large are the volume differences between `none` and `fast`?
Would you consider the result to be robust across our choices of patameters?

- 1's
- 10's
- 100's
- 1000's

<details>
<summary>Click to see answer</summary>

- 100's, I would not consider our result to be robust across our choices of parameters.

</details>