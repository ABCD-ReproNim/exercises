# Week 2 Quiz

### Quiz Instructions

In this Week 2 Quiz, we will ask you a few questions about ABCD Study data and you will complete a few exercises about shell and git basics.

If you have access to ABCD Study data, then we recommend that you also complete the Week 2 Bonus Quiz on DEAP (listed under Assignments). This bonus quiz is not required if you do not have access to ABCD data.

***

### ABCD Data Questions

First, please answer two questions about ABCD data.

**Question 1**
Genotyping is included in the ABCD tabulated data.

- True
- False

**Question 2**
What are some reasons to expect missing data in the ABCD dataset?
Select all that apply:

- Some measures are not taken at every time point
- Different protocols are implemented across different sites
- Some people miss appointments
- Sometimes data are deleted just for the fun of it
****
Let's do a few exercises using the Terminal

For students running computers with MacOS or Linux, follow the instructions in the lecture and do the following problems using your operating system’s Terminal application. For Windows users, you can download Ubuntu for Windows  [here](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:regionofsystemrequirementstab).

**Question 3**
Which command(s) will print what shell you’re currently in?
Select all that apply:

- `echo $shell`
- `echo $SHELL`
- `echo SHELL`
- `echo $SHELL > shell.txt | cat shell.txt`

**Question 4**
Grep is a bash command used to match patterns and expressions. Using only one line in the terminal, find how many lines contain the word “pattern” in the grep user manual.

Hint: you may need to use pipes.

- 55
- 28
- 32
- 18

**Question 5**
Using only commands in the Terminal application, create a directory called `week_2`. Within this directory, save the user manuals of the commands `grep`, `cat`, and `ls` to respective files called `grep.txt`, `cat.txt`, and `ls.txt`. Using one line in the Terminal, sort the contents of these three files by the number of lines they contain, in ascending order. What is this order?

- `cat.txt`, `grep.txt`, `ls.txt`
- `grep.txt`, `cat.txt`, `ls.txt`
- `ls.txt`, `cat.txt`, `grep.txt`
- They all have the same number of lines.

**Question 6**
Within the `week_2` directory, create a new directory called `user_manuals`. Which of the following commands will deposit `grep.txt`, `cat.txt`, and `ls.txt` into the `user_manuals` directory and remove them from the parent `week_2` directory? Run this command to deposit the files (if multiple options are true, only run one command).

- `cp *.txt user_manuals/`
- `cp grep.txt cat.txt ls.txt user_manuals/`
- `mv *.txt user_manuals/`
- `mv grep.txt cat.txt ls.txt user_manuals/`

***

Now let's do a few Git exercises

Install git on your local computer, if you do not already have it. Here are the [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)  for how to install git on all operating systems.

If you are running git for the first time (either on your local machine or remotely) you should configure your `user.name` and `user.email`. Please see this  [link](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)  for more information.

**Question 7**
Initialize a git repository within the `week_2` directory. Add the three files within the `user_manuals` directory.

Hint: you do not need to add each file separately.

After adding the three files, commit the files and tag the commit with a message of “added grep, cat, and ls manuals”.

After the commit, what is the status of the repository?

- On branch master. No commits yet. Untracked files in user_manuals/
- On branch master. No commits yet. Changes to be committed \<files in user_manuals/>
- On branch master. Nothing to commit. Working tree clean.
- On branch user_manuals. No commits yet. Changes to be committed \<files in user_manuals/>

**Question 8**
Create a branch called “new_feature”. Check the git log. Where is HEAD currently pointing?

- master
- working tree clean
- new_feature
- unstaged changes

**Question 9**
Checkout the new_feature branch. Using the Terminal, add the line of text “code for new feature” to a new file called `awesome_feature.txt`. Add `awesome_feature.txt` to the staging area and commit using the message “adding awesome feature”. Using git checkout, switch back to the master branch. Using commands in the Terminal.

How many lines does your git log currently have?

- 6
- 11
- 5
- 2