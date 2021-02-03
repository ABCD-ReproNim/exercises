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

Thus far in the course we've used `bash` to automate manual tasks,
`git` to keep track of changes, containers to isolate our software, and
[DataLad](https://www.datalad.org/) (tied together with `bash`, `git`, and containers) to run commands reproducibly.
[ReproMan](https://reproman.readthedocs.io/en/latest/) takes us a step further so that we can run commands _at scale_
(e.g., running the same command across many participants, on other machines,
and/or on a high performance/throughput computing cluster).

While not strictly necessary, we do recommend you complete the [week 8](https://github.com/ABCD-ReproNim/exercises/blob/main/week_8/week_8_quiz.md#repronim-questions) (DataLad) and [week 9 ](https://github.com/ABCD-ReproNim/exercises/blob/main/week_9/week_9_quiz.md#repronim-questions) (reproducible workflows) quizzes before completing this week's ReproNim questions. For today's ReproNim portion of the Data Exercise, you
will be cloning (via the command `datalad clone week9_analysis week10_analysis`), the same [Study Forrest dataset](https://github.com/psychoinformatics-de/studyforrest-data-structural) that we worked with in the ReproNim portions of the previous two quizzes.
We will also be testing different ways of using FSL's [`FIRST`](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST) again.

Enrolled Students: We recommend you use the online version of
the [ABCD-ReproNim Jupyterhub](https://docs.google.com/document/d/1kXvK2c_N9TkIAYn21WfzlCPtJvxhjW13Ftf0DwnAnlg/edit#heading=h.yb1hc7y3vc15), in
which DataLad is already installed. You can also use a local version of the ABCD-ReproNim JupyterHub container. Instructions on how to set up a local
instance of our JupyterHub can be found [here](https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439). Alternatively,
you can work with a local, non-JupyterHub instance of DataLad by following the installation
instructions [here](https://handbook.datalad.org/en/latest/intro/installation.html).

Observer Students: We recommend you use the ABCD-ReproNim JupyterHub container that we've set up for ABCD-ReproNim Observer Students, in which
DataLad is already installed. Instructions on how to set up a local instance of our JupyterHub can be
found [here](https://neurostars.org/t/using-abcd-repronim-jupyterhub-container-locally-via-docker/17439). General information about the
ABCD-ReproNim JupyterHub can be
found [here](https://docs.google.com/document/d/1kXvK2c_N9TkIAYn21WfzlCPtJvxhjW13Ftf0DwnAnlg/edit#heading=h.yb1hc7y3vc15). Alternatively, you can
work with a local, non-JupyterHub instance of DataLad by following the installation
instructions [here](https://handbook.datalad.org/en/latest/intro/installation.html).


**Question 6**

What can you do with ReproMan that you cannot do with DataLad?

- [ ] Track and commit commands and their output
- [ ] Type a command on one machine and have it run on another machine
- [ ] Run a command within a singularity container
- [ ] Parallelize a command by running it with different inputs


<details>
<summary>Click to see answer</summary>

ReproMan (but not DataLad) can:
- [x] Type a command on one machine and have it run on another machine
    - ReproMan can `ssh` into another computer
    and run a command for you (while still tracking and committing results)
- [x] Parallelize a command by running it with different inputs
    - While the command you run through DataLad could be parallelized, DataLad itself cannot parallelize your command.
      ReproMan, on the other hand, has specific flags (`--batch-spec` and `--batch-parameter`) to run the command with different inputs
      in parallel.

Both ReproMan and DataLad can:
  - [ ] Track and commit commands and their output
      - Both DataLad and ReproMan execute commands and create commits automatically.
  - [ ] Run a command within a singularity container
      - Both DataLad and ReproMan can run a command in a singularity container
          - DataLad Example:
              - `datalad create testrun && cd testrun`
              - `datalad containers-add hello-world --url shub://vsoch/hello-world`
              - `datalad containers-run  -n hello-world echo "example command"`
          - ReproMan Example (theoretical):
              - `datalad create testrun && cd testrun`
              - `reproman create hello-world -t singularity --backend-parameters image=shub://vsoch/hello-world`
              - `reproman run  --resource hello-world  --orc datalad-local-run echo "example command"`

***

</details>

**Question 7**

We will be making a new DataLad dataset named `week10_analysis`.
If you completed the [week 9 quiz](https://github.com/ABCD-ReproNim/exercises/blob/main/week_9/week_9_quiz.md#repronim-questions) and have a `week9_analysis` directory tree that looks like this,
```
- derivatives
    - first
        - ...
- data
    - sub-01
    - sub-02
```
the following commands _should_ get you up to speed:
- `datalad clone week9_analysis week10_analysis`
- `cd week10_analysis`

Assuming this is the case, after entering the above commands you _should_ be ready to continue with this question (but check `datalad status` within each dataset to see if there are uncommitted files!)

If you did _not_ complete the [week 9 quiz](https://github.com/ABCD-ReproNim/exercises/blob/main/week_9/week_9_quiz.md#repronim-questions) (or, if you'd just like a fresh start for this week),
then take a moment to look at the answer posted to Question 7 of the [week 9 quiz](https://github.com/ABCD-ReproNim/exercises/blob/main/week_9/week_9_quiz.md#repronim-questions). Enter those commands now, only changing instances
of `week9_analysis` with `week10_analysis`. This will set up the appropriate DataLad `week10_analysis` dataset needed to complete the rest of this week's questions.

If the `week10_analysis` dataset is clean, which of the following should the output of `datalad status` be? (if your dataset is not clean, use `datalad save` to
clean your datasets)

- [ ]
  ```
  modified: data (dataset)
  modified: derivatives (dataset)
  ```
- [ ]
  ```
  untracked: sub-01/anat/sub-01_T1w_to_std_sub.mat (file)untracked: sub-01/anat/sub-01_T1w_to_std_sub.nii.gz (file)
  modified: sub-01/anat/sub-01_T1w.nii.gz (file)
  ```
- [ ] `nothing to save, working tree clean`
- [ ]
  ```
  [ERROR  ] No dataset found at '<directory>'.  Specify a dataset to work with by providing its path via the 
  `dataset` option, or change the current working directory to be in a dataset. [dataset.py:require_dataset:569] (NoDatasetFound)
  usage: datalad status [-h] [-d DATASET] [--annex [MODE]] [--untracked MODE] [-r] [-R LEVELS] [-e {no|commit|full}] [-t {raw|eval}]
                      [PATH [PATH ...]]
  ```
<details>
<summary>Click to see answer</summary>

    - `nothing to save, working tree clean`

  The working tree refers to your series of commits, the fact that
  the working tree is clean means there are no new/modified files
  that Datalad does not know about.

***

</details>

**Question 8**

In this question, we're not going to use ReproMan to run commands on an
Amazon Web Services server or a high performance computing cluster. Instead
we are only going to use the machine at our disposal.
However, once you practice the syntax of ReproMan, changing
the command from running commands locally to running commands on a highly
powered machine halfway across the country will be straightforward.
Lets see how...

First, we need to create what ReproMan calls a `resource`.
A resource can be your own computer, a singularity
image, some other computer in a closet, or an instance from
Amazon.

In this example, we will call our resource `my-local-shell`. Unscramble
the below command to create our resource.
- `reproman shell create --resource-type my-local-shell`

Once you are successful, the output of `reproman ls` should list your newly created resource (your shell):
```
RESOURCE NAME        TYPE                 ID                  STATUS    
-------------        ----                 --                  ------    
my-local-shell         shell                a8b86830-64b4-11eb- available
```

## Note:
Look at the [ReproMan documentation](https://reproman.readthedocs.io/en/latest/generated/man/reproman-create.html) for help with using this command.

<details>
<summary>Click to see answer</summary>

- `reproman create my-local-shell --resource-type shell`

***

</details>

**Question 9**

In [last week's quiz](https://github.com/ABCD-ReproNim/exercises/blob/main/week_9/week_9_quiz.md#repronim-questions), you ran a separate DataLad command for each
set of inputs (e.g., the participant parameters (`01`, `02`) and the method parameters (`none`, `fast`)),
resulting in four total commands you had to type out.
ReproMan can condense those four commands into one call that runs all desired commands in parallel.
In the following command, the arguments are in the correct order but the
names of the flags are not provided.
Use the flag bank below to place the flags in the correct positions
in the `reproman run` command. **NOTE**: Some flags may be used more than once.
Look at the [ReproMan documentation](https://reproman.readthedocs.io/en/latest/generated/man/reproman-run.html) for help.

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
__[insert flag]__ my-local-shell \
__[insert flag]__ local \
__[insert flag]__ datalad-no-remote \
__[insert flag]__ container=fsl \
__[insert flag]__ 'subject=01,02' \
__[insert flag]__ 'method=none,fast' \
__[insert flag]__ data/sub-'{p[subject]}'/anat/sub-'{p[subject]}'_T1w.nii.gz \
__[insert flag]__ derivatives/sub-'{p[subject]}'/'{p[method]}' \
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

In order to run the previous ReproMan command on remote computer,
which flags would need to change values? (at a minimum)

- [ ] `--resource, --submitter, --orchestrator`
- [ ] `--resource`
- [ ] `--submitter`
- [ ] `--orchestrator`
- [ ] `--resource, --orchestrator`
- [ ] `--resource, --submitter`
- [ ] `--submitter, --orchestrator`

<details>
<summary>Click to see answer</summary>

- `--resource, --orchestrator`
    - The resource needs to change from `my-local-shell` to a reference to the remote machine
      that you can `ssh` into.
    - The orchestrator needs to change since `datalad-no-remote` is specific to one's local shell.
    - The submitter can remain the same since you may be able to submit jobs using the shell
      on the remote computer.

</details>
