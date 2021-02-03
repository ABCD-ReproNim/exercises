# Week 10 Quiz

### Quiz Instructions

In this Week 10 Quiz, we will ask you a few questions about [ABCD Novel Technologies and using ReproMan Execution and Environment Manager](https://abcd-repronim.github.io/materials/week-10/).

***

## ABCD questions

**Question 1**

Mobile and wearable technology data are acquired using which of the following methods? (select all that apply)

- [ ] Fitbit Charge 2
- [ ] Daily self report survey of physical activity
- [ ] Effortless Assessment of Risk States (EARS) smartphone app
- [ ] Self report of screen media activity
- [ ] Parent report of screen media activity

<details>
<summary>Click to see answer</summary>

- Fitbit Charge 2
- Effortless Assessment of Risk States (EARS) smartphone app
- Self report of screen media activity
- Parent report of screen media activity

***

</details>

**Question 2**

Unprocessed minute-level activity data are available in the Data Releases.

- True
- False

<details>
<summary>Click to see answer</summary>

- False

Unprocessed data are available from the data analysis and informatics core, not the regular data releases.

***

</details>

**Question 3**

Mobile device data capture using the EARS app is possible on which of the following operating systems? (select all that apply)

- [ ] iOS
- [ ] Android
- [ ] Chrome OS
- [ ] Windows

<details>
<summary>Click to see answer</summary>

- Android

***

</details>

**Question 4**

Summary data from the EARS app are available from which of the following categories? (select all that apply)

- [ ] Social media
- [ ] Podcasts
- [ ] Gaming
- [ ] Productivity
- [ ] YouTube

<details>
<summary>Click to see answer</summary>

- Social media
- Gaming
- YouTube

***

</details>

**Question 5**

Self-report data are acquired…

- Every 3 months
- Every year
- Every other year
- Every two years

<details>
<summary>Click to see answer</summary>

- Every year

***

</details>

## ReproNim questions

We have covered: bash to automate manual tasks, git to keep track of changes, containers to isolate our software, and datalad tied together bash, git, and containers to run commands reproducibly.
Reproman takes us a step further to run commands at scale
(e.g., running the same command across many participants, running the command on another machine,
and/or running the command on a high performance/throughput computing cluster).

For today's Repronim questions, you will be cloning
(via the command `datalad clone week9_analysis week10_analysis`, assuming you completed [the week 9 quiz](../week9/week_9_quiz.md#repronim-questions)),
which covered the [Study Forrest dataset](https://github.com/psychoinformatics-de/studyforrest-data-structural) we worked with in the Repronim portions of the previous two quizes.
We will also be testing different ways of using FSL's [`FIRST`](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST) again.

Enrolled Students: We recommend you use the online version of
the [ABCD-ReproNim Jupyterhub](https://docs.google.com/document/d/1kXvK2c_N9TkIAYn21WfzlCPtJvxhjW13Ftf0DwnAnlg/edit#heading=h.yb1hc7y3vc15), in
which DataLad is already installed. You can also use a local version of the ABCD-ReproNim JupyterHub container. Instructions on how to set up a local
instance of our JupyterHub can be found [here](https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439). Alternatively,
you can work with a local, non-JupyterHub instance of DataLad by following the installation
instructions [here](https://handbook.datalad.org/en/latest/intro/installation.html).

Observer Students: We recommend you use the ABCD-ReproNim Jupyterhub container that we've set up for ABCD-ReproNim Observer Students, in which
DataLad is already installed. Instructions on how to set up a local instance of our JupyterHub can be
found [here](https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439). General information about the
ABCD-ReproNim JupyterHub can be
found [here](https://docs.google.com/document/d/1kXvK2c_N9TkIAYn21WfzlCPtJvxhjW13Ftf0DwnAnlg/edit#heading=h.yb1hc7y3vc15). Alternatively, you can
work with a local, non-JupyterHub instance of DataLad by following the installation
instructions [here](https://handbook.datalad.org/en/latest/intro/installation.html).


**Question 6**

What can you do with Reproman that you cannot do with Datalad?

- [ ] Track and commit commands and their output
- [ ] Type a command on one machine and have it run on another machine
- [ ] Run a command within a singularity container
- [ ] Parallelize a command by running it with different inputs


<details>
<summary>Click to see answer</summary>

- [ ] Track and commit commands and their output
    - Both Datalad and Reproman execute commands and create commits automatically.
- [x] Type a command on one machine and have it run on another machine
    - Reproman can `ssh` into another computer
    and run a command for you (while still tracking and committing results)
- [ ] Run a command within a singularity container
    - Both Datalad and Reproman can run a command in a singularity container
        - Datalad Example:
            - `datalad create testrun && cd testrun`
            - `datalad containers-add hello-world --url shub://vsoch/hello-world`
            - `datalad containers-run  -n hello-world echo "example command"`
        - Reproman Example (theoretical):
            - `datalad create testrun && cd testrun`
            - `reproman create hello-world -t singularity --backend-parameters image=shub://vsoch/hello-world`
            - `reproman run  --resource hello-world  --orc datalad-local-run echo "example command"`

- [x] Parallelize a command by running it with different inputs
    - While the command you run through Datalad could be parallelized, Datalad itself cannot parallelize your command.
      Reproman, on the other hand, has specific flags (`--batch-spec` and `--batch-parameter`) to run the command with different inputs
      in parallel.
***

</details>

**Question 7**

We will be making a new datalad dataset named `week10_analysis`,
If you completed `week 9`, the following commands _should_ get you up to speed.
- `datalad clone week9_analysis week10_analysis`
- `cd week10_analysis`
Assuming you have a directory tree that looks like this:
```
- derivatives
    - first
        - ...
- data
    - sub-01
    - sub-02
```
You _should_ be ready to continue (check `datalad status` within each dataset to see if there are uncommitted files!).
If you did not start the week 9 quiz (or you would like a fresh start),
look at the answer for question 7 and copy those commands, only changing instances
of `week9_analysis` with `week10_analysis`.

If the `week10_analysis` dataset is clean, what should the output of `datalad status` be?
(if your dataset is not clean, use `datalad save` to
clean your datasets)
- ```
  modified: data (dataset)
  modified: derivatives (dataset)
  ```
- ```
  untracked: sub-01/anat/sub-01_T1w_to_std_sub.mat (file)untracked: sub-01/anat/sub-01_T1w_to_std_sub.nii.gz (file)
  modified: sub-01/anat/sub-01_T1w.nii.gz (file)
  ```
- `nothing to save, working tree clean`
- ```
  [ERROR  ] No dataset found at '<directory>'.  Specify a dataset to work with by providing its path via the `dataset` option, or change the current working directory to be in a dataset. [dataset.py:require_dataset:569] (NoDatasetFound)
  usage: datalad status [-h] [-d DATASET] [--annex [MODE]] [--untracked MODE] [-r] [-R LEVELS] [-e {no|commit|full}] [-t {raw|eval}]
                      [PATH [PATH ...]]
  ```
<details>
<summary>Click to see answer</summary>

Answer:
    - `nothing to save, working tree clean`
        - The working tree refers to your series of
          commits, the fact that the working tree is clean
          means there are no new/modified files that Datalad
          does not know about.
***

</details>

**Question 8**

In this example usage of Reproman, we are not going to use
amazon web services or a high performance computing cluster,
we are only going to use the machine at our disposal.
However, once you practice the syntax of Reproman, changing
the command from running locally to an overpowered machine
halfway across the country will be straightforward.

First, we need to create what Reproman calls a `resource`,
where the resource can be your own computer, a singularity
image, some other computer in a closet, or an instance from
Amazon.

We will call our resource `my-local-shell`, unscramble
the below command to create our resource.
- `reproman shell create --resource-type my-local-shell`

Once you are successful, the output of `reproman ls` should list your newly created resource (your shell):
```
RESOURCE NAME        TYPE                 ID                  STATUS    
-------------        ----                 --                  ------    
my-local-shell         shell                a8b86830-64b4-11eb- available 
```

## Note:
[Look at Reproman's documentation for help](https://reproman.readthedocs.io/en/latest/generated/man/reproman-create.html)

<details>
<summary>Click to see answer</summary>

- `reproman create my-local-shell --resource-type shell`

***

</details>

**Question 9**

In last weeks quiz (week 9), you ran a separate Datalad command for each
set of inputs (changing the participant (01,02) and the method (none,fast)),
resulting in 4 total commands if you typed them all out.
Reproman can condense those 4 commands into one call that runs all 4 commands in parallel.
I've supplied the arguments in a correct order, but I did not give the names of the flags
in the command.
Use the flag bank below to place the flags in the correct positions
in the `reproman run` command. **NOTE**: Some flags may be used more than once.
Look at the [reproman documentation](https://reproman.readthedocs.io/en/latest/generated/man/reproman-run.html) for help.

#### Flag Bank
- `--output`
- `--resource`
- `--submitter`
- `--batch-parameter`
- `--orchestrator`
- `--job-parameter`
- `--input`



```
reproman run  \
________ my-local-shell \
________ local \
________ datalad-no-remote \
________ container=fsl \
________ 'subject=01,02' \
________ 'method=none,fast' \
________ data/sub-'{p[subject]}'/anat/sub-'{p[subject]}'_T1w.nii.gz \
________ derivatives/sub-'{p[subject]}'/'{p[method]}' \
bash -c "cd data/sub-'{p[subject]}'/anat && run_first_all -i sub-'{p[subject]}'_T1w.nii.gz -o ../../../derivatives/first/sub-'{p[subject]}'/'{p[method]}' -m '{p[method]}' -s L_Hipp,R_Hipp"
```

<details>
<summary>Click to see answer</summary>

```
reproman run  \
--resource my-local-shell \
--submitter local \
--orchestrator datalad-no-remote \
--job-parameter container=fsl \
--batch-parameter 'subject=01,02' \
--batch-parameter 'method=none,fast' \
--input data/sub-'{p[subject]}'/anat/sub-'{p[subject]}'_T1w.nii.gz \
--output derivatives/sub-'{p[subject]}'/'{p[method]}' \
bash -c "cd data/sub-'{p[subject]}'/anat && run_first_all -i sub-'{p[subject]}'_T1w.nii.gz -o ../../../derivatives/first/sub-'{p[subject]}'/'{p[method]}' -m '{p[method]}' -s L_Hipp,R_Hipp"
```

</details>

**Question 10**

In order to run the previous Reproman command on remote computer,
which flags would need to change values? (at a minimum).

- `--resource, --submitter, --orchestrator`
- `--resource`
- `--submitter`
- `orchestrator`
- `--resource, --orchestrator`
- `--resource, --submitter`
- `--submitter, --orchestrator`

<details>
<summary>Click to see answer</summary>

- `--resource, --orchestrator`
    - The resource needs to change from `my-local-shell` to a reference to the remote machine
      that you can ssh into.
    - The orchestrator needs to change since `datalad-no-remote` is specific to one's local shell.
    - The submitter can remain the same since you may be able to submit jobs using the shell
      on the remote computer.

</details>
