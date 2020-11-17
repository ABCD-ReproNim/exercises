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
Let's do a few exercises using the Terminal

For students running computers with MacOS or Linux, follow the instructions in the lecture and do the following problems using your operating system’s Terminal application. For Windows users, you can download Ubuntu for Windows  [here](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:regionofsystemrequirementstab).

**Question 3**

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

**Question 4**

Grep is a bash command used to match patterns and expressions. Using only one line in the terminal, find how many lines contain the word “pattern” in the grep user manual.

Hint: you may need to use pipes.

- 55
- 28
- 32
- 18

<details>
<summary>Click to see answer</summary>

28

**Note**

Your answer will depend on your operating system. The answer of 28 lines was found using Mac OS 10.14.6.

**Possible solutions**

`man grep | grep pattern | wc -l`

`man grep | grep -c pattern`

**Explaination**

`man` is the shell command to see a commands user manual. `grep` is used here in two ways. First we print the user manual of `grep` using `man grep`. Then, that output is piped (using `|`) to the `grep` command and we search for all instances of the string `pattern`. This narrows down the `grep` user manual to only the lines that include `pattern`. We then pipe (using `|`) this output into the `wc` program, which counts various aspects of the input. We us `-l` to tell `wc` that we want to count the number of lines. The second solution, `man grep | grep -c pattern`, leverages the `-c` option in grep, which also counts the number of lines in the matching output.

Note: the usage of `grep pattern` is case-insensitive and can contain the plural, thus `Pattern`, `Patterns`, and `patterns` are also included.

***

</details>

**Question 5**

Using only commands in the Terminal application, create a directory called `week_2`. Within this directory, save the user manuals of the commands `grep`, `cat`, and `ls` to respective files called `grep.txt`, `cat.txt`, and `ls.txt`. Using one line in the Terminal, sort the contents of these three files by the number of lines they contain, in ascending order. What is this order?

- `cat.txt`, `grep.txt`, `ls.txt`
- `grep.txt`, `cat.txt`, `ls.txt`
- `ls.txt`, `cat.txt`, `grep.txt`
- They all have the same number of lines.

<details>
<summary>Click to see answer</summary>

`cat.txt`, `grep.txt`, `ls.txt`

**Note**

Your answer will depend on your operating system. The answer of `cat.txt`, `grep.txt`, `ls.txt` was found using Mac OS 10.14.6.

**Possible solutions**

`wc -l *.txt | sort`

`wc -l *.txt > lines.txt | sort lines.txt`

**Explanation**

`wc` is the bash program that counts things. With the `-l` option, we tell `wc` to count the number of lines. `*.txt` uses the wildcard operator, `*`, to find all files that end in `.txt`, that is, the three files you created in the previous question. So, `wc -l *.txt` counts the number of lines in all files that end in `.txt`. Note, it is implicit in the way this `wc` command is structured that `wc` will only look for matches in the current directory.

We then pipe the output of `wc` to the `sort` command, to have it sort by line number. In the `wc -l *.txt > lines.txt | sort lines.txt` solution, we have an intermediary step of writing the line numbers to a file called `lines.txt`.

***

</details>

**Question 6**

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

<details>
<summary>Click to see answer</summary>

On branch master. Nothing to commit. Working tree clean.

**Solution**

Initialize the git repository: `git init`

Add the three files within the `user_manuals` directory: `git add user_manuals/*.txt`

Commit the files: `git commit -m "added grep, cat, and ls manuals"`

Check the status of the repository: `git status`

***

</details>

**Question 8**

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

**Question 9**

Checkout the new_feature branch. Using the Terminal, add the line of text “code for new feature” to a new file called `awesome_feature.txt`. Add `awesome_feature.txt` to the staging area and commit using the message “adding awesome feature”. Using git checkout, switch back to the master branch. Using commands in the Terminal.

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

Commit: `git commit -m "adding awesome feature`

Checkout master: `git checkout master`

View log: `git log`

Count number of lines in log: `git log | wc -l`

Your log should look something like (with a different commit ID):

```
commit 63a47a48c7673f87b7c8ab463fa766dee3b485e7 (HEAD -> master)
Author: user.name <user.email>
Date:   DATE

    added grep, cat, and ls manuals
```

***

</details>
