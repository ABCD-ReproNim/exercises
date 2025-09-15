# Week 2 Quiz

### Quiz Instructions

In this Week 2 Quiz, we will ask you a few questions about ABCD Study data and you will complete a few exercises about shell and git basics.

If you have access to ABCD Study data, then we recommend that you also complete the Week 2 Bonus Quiz on DEAP. This bonus quiz is not required if you do not have access to ABCD data.

***

### ABCD Data Questions

First, please answer two questions about ABCD data.

**Question 1**

Genotyping is included in the ABCD tabulated data.

- True
- False

<details>
<summary>Click to see answer</summary>

False

***

</details>

**Question 2**

What are some reasons to expect missing data in the ABCD dataset?
Select all that apply:

- Some measures are not taken at every time point
- Different protocols are implemented across different sites
- Some people miss appointments
- Sometimes data are deleted just for the fun of it

<details>
<summary>Click to see answer</summary>

Some measures are not taken at every time point

Some people miss appointments

</details>

****

### DEAP Questions

Let's do a few exercises in the DEAP dataset creation portal

Go to [DEAP](https://abcd.deapscience.com/), and click "Create a dataset" to begin exploring the data dictionary.

**Question 3**

First find the scores for the NIH Toolbox Oral Reading Recognition Test Age 3+ v2.0, Age-Corrected Standard Score.

Hint: In the DEAP ABCD Ontology, all of the measures from this test have the prefix “nc_y_nihtb_readr.”

What is the mean age-corrected standard score at baseline?

- 101.653
- 104.974
- 102.517
- 105.746

<details>
<summary>Click to see answer</summary>

102.517

</details>

**Question 4**

Identify the variable representing average fractional anisotropy within the left inferior longitudinal fasciculus.

Hint: This variable went by the name of “dmri_dti.fa_fiber.at_ilf.lh” in the DEAP 1.0.

How many participants have complete data for this variable at the ses-04A timepoint?

- 11130
- 3969
- 7841
- 6224

<details>
<summary>Click to see answer</summary>

6224

</details>

**Question 5**

Navigate to the table for the Emotional Stroop Task. Are there any responsible data use warnings or data quality warnings? If so, what are the recommendations for appropriate use?  

- There are no warnings about using these variables.
- Researchers should use pre-set cut-offs to omit RTs above and below specific thresholds and should consider downloading trial-wise data to recalculate mean RTs after excluding outlier trials.
- Data from this task may be culturally biased and should be analyzed with appropriate considerations
- Researchers should exclude participants whose data contains outlier RTs

<details>
<summary>Click to see answer</summary>

Researchers should use pre-set cut-offs to omit RTs above and below specific thresholds and should consider downloading trial-wise data to recalculate mean RTs after excluding outlier trials.

To view this information, click the "Details" button for any of the Emotional Stroop Task variables. You should see a warning triangle followed by the following sentence: 

Learn about data quality issues with this variable [here](https://docs.abcdstudy.org/latest/documentation/non_imaging/nc.html#data-est).

Click on the link at the end of the sentence to view data quality warnings.

</details>

### Shell Basics

Let's do a few exercises using the Terminal

For students running computers with MacOS or Linux, follow the instructions in the lecture and do the following problems using your operating system’s Terminal application. For Windows users, you can download Ubuntu for Windows [here](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:regionofsystemrequirementstab). You can also practice using bash commands without downloading Ubuntu via an online Linux Terminal application such as [Webminal](https://www.webminal.org/terminal/) (note: you will need to create a free user account in order to use this online Linux emulator).

**Question 6**

Which command(s) will print what shell you’re currently in?
Select all that apply:

- `echo $shell`
- `echo $SHELL`
- `echo SHELL`
- `echo $SHELL > shell.txt | cat shell.txt`

<details>
<summary>Click to see answer</summary>

`echo $SHELL`

`echo $SHELL > shell.txt | cat shell.txt`

**Note**

`echo $SHELL > shell.txt | cat shell.txt` is an intentionally convoluted and unnecessary solution meant to explain shell concepts.

**Explanation**

`echo` is the bash shell command that prints the input back to the terminal. `$` is used to call on existing variables in the namespace. `SHELL` is a default environment variable that encodes the type of shell currently running. Thus, `echo $SHELL` will print the contents of the environment variable to the terminal.

`>` is an operator that funnels the output of the preceding command into a text file rather than to the terminal. `|` is a pipe operator that takes the output of the preceding command as the input into the next. `cat` is the bash command that prints the contents of a text file to the terminal screen. Thus, `echo $SHELL > shell.txt | cat shell.txt` funnels the output of `echo $SHELL` into a text file called `shell.txt` and then `cat shell.txt` prints the contents of `shell.txt` to the terminal.

***

</details>

**Question 7**

Grep is a bash command used to match patterns and expressions. Using only one line in the terminal, find how many times the word “pattern” appears in the grep user manual.

Hint: you may need to use pipes.

- 36
- 28
- 39
- Some other value not listed here

<details>
<summary>Click to see answer</summary>

The numerical answer to this question depends on which version of grep you are running in your Terminal. If you are running `grep` on a Mac (i.e., are running BSD grep 2.5.1-FreeBSD or similar) the number of times the word "pattern" appears in the grep user manual is 35. If you are running `grep` on a Linux Terminal (i.e., are running GNU grep 2.20 or similar) the answer is 22. If you are running a version of grep that is different from either of the above then you may have another answer! Because of this all answers to this question are marked as correct. The important thing here is not, in fact, to identify how many instances of the word "pattern" appear in the grep user manual (shocker!)... what is important is to understand how to use `grep` to search for specific expressions. A detailed explanation of one possible set of commands that achieve the above desired search is described below.
    
**Possible solution**

`man grep | grep -i -o pattern | wc -l`
    
**Explanation**
    
`man` is the shell command used to see a commands user manual. `grep` is used here in two ways. First we print the grep user manual using `man grep`. Then, that output is piped (using `|`) to the `grep` command where we search for all instances of the string `pattern`. The `grep` option `-i` is selected to ignore capitalization (`grep` is case-sensitive by default, so `-i` tells `grep` to return instances of the strings `pattern`, `Pattern`, `PATTERN`, etc). We also use the option `-o` to ask `grep` to print out each instance of `pattern` on a new line (without the `-o` flag, `grep` would print out each line that contains *one or more* instance of the string `pattern` -- because we want to count the *total number of times* the word "pattern" appears, we want to print each appearing of `pattern` to a new line). Finally, We pipe (using `|`) this output into the `wc` program, which counts various aspects of the input. We use `-l` to tell `wc` that we want to count the number of lines (each of which contains a new instance of `pattern`).

If you want to know more about the available options in `grep`, `wc`, or any other bash command then you can find a description of all options in the manual files.
    
Note: the usage of `grep -i -o pattern` can contain the plural, thus `pattern` and `patterns` are both included.
      
***

</details>

**Question 8**

Using only commands in the Terminal application, create a directory called `week_2`. Within this directory, save the user manuals of the commands `grep`, `cat`, and `ls` to respective files called `grep.txt`, `cat.txt`, and `ls.txt`. Using one line in the Terminal, sort the contents of these three files by the number of lines they contain, in ascending order. What is this order?

- `cat.txt`, `grep.txt`, `ls.txt`
- `cat.txt`, `ls.txt`, `grep.txt`
- `ls.txt`, `cat.txt`, `grep.txt`
- some other combination not listed here.

<details>
<summary>Click to see answer</summary>

Your answer will depend on your operating system/which version of Unix or Linux you are using. The answer `cat.txt`, `grep.txt`, `ls.txt` was found using the FreeBSD version of Unix that runs on Mac OSX. The answer of `cat.txt`, `ls.txt`, `grep.txt` was found using the version of Linux that runs on CentOS 7 and Fedora 31. There are other possibilities, thus all answers to this question are marked as correct.

**Possible solutions**
    
You can create a new directory called `week_2` via the command `mkdir week_2`. You can then change you working directory to `week_2` by using the command `cd week_2`. The separate commands `man ls > ls.txt`, `man grep > grep.txt`, and `man cat > cat.txt` would create three txt files within `week_2`, each containing the three different user manuals for `ls`, `grep` and `cat`. Next you can print a sorted list of the number of lines within each user manual using `wc -l *.txt | sort`. Note, as before, there are many different ways you could determine the answer to this questions. The above is just one example.

**Explanation**

`wc` is the bash program that counts things. With the `-l` option, we tell `wc` to count the number of lines. `*.txt` uses the wildcard operator, `*`, to find all files that end in `.txt`, that is, the three files you created in the previous question. So, `wc -l *.txt` counts the number of lines in all files that end in `.txt`. Note, it is implicit in the way this `wc` command is structured that `wc` will only look for matches in the current directory.

We then pipe the output of `wc` to the `sort` command, to have it sort by line number. In the `wc -l *.txt > lines.txt | sort lines.txt` solution, we have an intermediary step of writing the line numbers to a file called `lines.txt`.

***

</details>

**Question 9**

Within the `week_2` directory, create a new directory called `user_manuals`. Which of the following commands will deposit `grep.txt`, `cat.txt`, and `ls.txt` into the `user_manuals` directory and remove them from the parent `week_2` directory? Run this command to deposit the files (if multiple options are true, only run one command).

- `cp *.txt user_manuals/`
- `cp grep.txt cat.txt ls.txt user_manuals/`
- `mv *.txt user_manuals/`
- `mv grep.txt cat.txt ls.txt user_manuals/`

<details>
<summary>Click to see answer</summary>

`mv *.txt user_manuals/`

`mv grep.txt cat.txt ls.txt user_manuals/`

**Explanation**

`mv` is the bash command to move files from one place to another. It can also be used to rename files if you specify the same location for the output. `mv` is not to be confused with `cp`, `mv` moves files whereas `cp` copies them. The distinction is that with `mv` your file will not exist in it's previous location whereas with `cp` it will.

You can use a wildcard operator to move all files that end in `*.txt` as in the `mv *.txt user_manuals/` solution. Or, you can specify each file manually, as in the `mv grep.txt cat.txt ls.txt user_manuals/` solution.

</details>

***

### Git Basics

Now let's do a few Git exercises

Install git on your local computer, if you do not already have it. Here are the [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  for how to install git on all operating systems.

If you are running git for the first time (either on your local machine or remotely) you should configure your `user.name` and `user.email`. Please see this  [link](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)  for more information.

**Question 10**

Initialize a git repository within the `week_2` directory. Add the three files within the `user_manuals` directory.

Hint: you do not need to add each file separately.

After adding the three files, commit the files and tag the commit with a message of “add grep, cat, and ls manuals”.

After the commit, what is the status of the repository?

- On branch master. No commits yet. Untracked files in user_manuals/
- On branch master. No commits yet. Changes to be committed \<files in user_manuals/>
- On branch master. Nothing to commit. Working tree clean.
- On branch user_manuals. No commits yet. Changes to be committed \<files in user_manuals/>

<details>
<summary>Click to see answer</summary>

On branch master. Nothing to commit. Working tree clean.

**Solution**

Initialize the git repository: `git init`

Add the three files within the `user_manuals` directory: `git add user_manuals/*.txt`

Commit the files: `git commit -m "add grep, cat, and ls manuals"`

Check the status of the repository: `git status`

***

</details>

**Question 11**

Using `git branch`, create a branch called “new_feature”. Check the git log. Where is HEAD currently pointing?

- master
- working tree clean
- new_feature
- unstaged changes

<details>
<summary>Click to see answer</summary>

master

**Solution**

Create new branch: `git branch new_feature`

Check the status `git status` and see that you're still on the master branch.

**Explanation**

`git branch new_feature` creates the branch called `new_feature`, however the `HEAD` is not yet pointed at the `new_feature` branch. The branch has been created, but the `HEAD` is still at the master branch. To move `HEAD` to the `new_feature` branch, you'd use `git checkout new_feature`.

Or, a related solution would be to use `git checkout -b new_feature`, which would create the branch and move `HEAD` all in one move.

***

</details>

**Question 12**

Checkout the new_feature branch. Using the Terminal, add the line of text “code for new feature” to a new file called `awesome_feature.txt`. Add `awesome_feature.txt` to the staging area and commit using the message “add awesome feature”. Using git checkout, switch back to the master branch. Using commands in the Terminal.

How many lines does your git log currently have?

- 6
- 11
- 5
- 2

<details>
<summary>Click to see answer</summary>

5

**Solution**

Checkout `new_feature`: `git checkout new_feature`

Create new file: `echo code for new feature > awesome_feature.txt`

Add to staging area: `git add awesome_feature.txt`

Commit: `git commit -m "add awesome feature`"

Checkout master: `git checkout master`

View log: `git log`

Count number of lines in log: `git log | wc -l`

Your log should look something like (with a different commit ID):

```
commit 63a47a48c7673f87b7c8ab463fa766dee3b485e7 (HEAD -> master)
Author: user.name <user.email>
Date:   DATE

    add grep, cat, and ls manuals
```

***

</details>
