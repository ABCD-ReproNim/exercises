# Week 14 Quiz

### Quiz Instructions

In this Week 14 Quiz, we will ask you a few questions about Statistical Considerations II and Visualizing Data. We will use some python packages and continue practicing using Datalad.

***

### ABCD Questions

**Question 1**

 How large do brain-behavior effect sizes tend to be in ABCD data?
   
   -small
   
   -medium
   
   -large


<details>
<summary>Click to see answer</summary>

small


***

</details>

**Question 2**

Which of these options was NOT listed as a possible reason for the "replication crisis"?

  -Sample size
  
  -Univariate vs. Multivariate methods
  
  -Variation of imaging/behavioral measures
  
  -Lack of precision in MRI imaging


<details>
<summary>Click to see answer</summary>
Lack of precision in MRI imaging


****

</details>

**Question 3**

True or False? For brain imaging ABCD data, tabulated ROI-based data is the most fine-grain data available.

<details>
<summary>Click to see answer</summary>
False


***

</details>

**Question 4**

What are some of the advantages of using multivariate methods as opposed to univariate methods when studying general cognition? *Select all that apply*

-You do not need to test 1000s of individuals
  
-Replication samples do not need to be extremely large

-Multivariate methods more accurately reflect how the brain functions

-Models can be more easily interpreted 



<details>
<summary>Click to see answer</summary>
  
-You do not need to test 1000s of individuals
  
-Replication samples do not need to be extremely large

-Multivariate methods more accurately reflect how the brain functions


***

</details>

**Question 5**

What is the bidirectional benefit of data in ABCD and other studies?

-ABCD data can be used to benchmark smaller independent samples

-Data from ABCD and other studies can be used to inform each other

-Data from smaller studies can be used to direct investigations in ABCD

-Both ABCD and other data can be combined into one large study


<details>
<summary>Click to see answer</summary>
  
Data from ABCD and other studies can be used to inform each other

***

</details>

### ReproNim Questions: Data Visualization in Python and Datalad

We recommend you use the ABCD-ReproNim Jupyterhub container that we've set up for ABCD-ReproNim Students, in which the appropriate libraries used in the Notebook have already been installed. 

Instructions on how to set up a local instance of our JupyterHub can be found [here](https://github.com/ABCD-ReproNim/exercises/blob/main/local_jupyter_hub.md)


Although running your analyses in scripts as opposed to Jupyter notebooks makes your work more easily reproducible, you can use a Jupyter notebook to get a feel for how you can use Seaborn. Create a notebook, import the Seaborn library, and load up the `penguins` dataset built into Seaborn. 

*sns.set_context just makes sure all of our plots have the same size and font

```
  import seaborn as sns
  import pandas as pd
  sns.set_context('notebook' , font_scale=1.5)
  data = sns.load_dataset('penguins')
  data.head()
```
The `load_dataset` function of Seaborn automatically loads the datasets up as Pandas Dataframes, which we can then inspect. We see that data has the following columns: `species`, `island`, `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`, `sex`.

We also notice that there are some `NaN` values...which would pose a problem if we wanted to run any actual statistical analyses on this data. We will use Sklearn to handle the missing values. We will do so by by imputing missing values in each column by the most frequenly occuring value in that column. Note: this is just one possible strategy and is not one that should be used in all situations.

```
  from sklearn.impute import SimpleImputer
  imputer = SimpleImputer(strategy='most_frequent')
  data.iloc[:,:] = imputer.fit_transform(data)
```

**Question 6**

 How would you visualize the relationship between bill length and flipper length separately for each species while ensuring that the x and y axes are not shared across the subplots and the colors are different across the subplots?

 -sns.regplot(x="flipper_length_mm", y="bill_depth_mm")
 
 -sns.lmplot(x="bill_length_mm", y="flipper_length_mm", col="species", hue="species", data=data, facet_kws={'sharey': False, 'sharex': False})

 -sns.lmplot(x="flipper_length_mm", y="bill_depth_mm", col="species", data=data)

<details>
<summary>Click to see answer</summary>
  
-sns.lmplot(x="bill_length_mm", y="flipper_length_mm", col="species", hue="species", data=data, facet_kws={'sharey': False, 'sharex': False})

![penguin3](https://github.com/user-attachments/assets/925795d6-3186-47bd-bb3d-a0d65e82ca13)

***

</details>

**Question 7**

In the previous question, we compared only bill length and flipper length. Now we would like to look at all of the variables compared to each other. To do this, we will use the pairplot function in seaborn. 
Using the [documentation](https://seaborn.pydata.org/generated/seaborn.pairplot.html), which code snippet creates a pairplot to compare each variable and ensure the species have different colors. **Select all that apply**

-sns.pairplot(data)

-sns.pairplot(data, hue='species')

-sns.pairplot(data, palette='Dark1')

-sns.pairplot(data, hue='species', palette='Dark2')

<details>
<summary>Click to see answer</summary>

-sns.pairplot(data, hue='species')

-sns.pairplot(data, hue='species', palette='Dark2')

![penguinbefore](https://github.com/user-attachments/assets/1bd678c5-1535-4393-a428-b6035ef0070e)

![penguinafter](https://github.com/user-attachments/assets/cb30ceda-61f2-446d-ab6c-494ed50447e2)


***

</details>

Next we'll look at using datalad to create a reproducible paper example with a pairplot. It may not surprise you to learn that DataLad can help you write a fully reproducible paper. In this example, we will automatically download an iris dataset, analyze the data, plot the data, and produce a readable PDF all using datalad. You can read more about this in the [DataLad handbook](http://handbook.datalad.org/en/latest/usecases/reproducible-paper.html). We will use the DataLad ["Automatically Reproducible Paper Template"](https://github.com/datalad-handbook/repro-paper-sketch/). The next two questions help you explore how to do this.

In a new directory, clone the example paper using the following command in the console:

```
  datalad clone https://github.com/datalad-handbook/repro-paper-sketch.git
```

Because this is an older example, there are three things we have to do to get this working properly.

1) Update git-annex
2) Change requirements.txt
3) Start a virtual environment

Please follow the next steps carefully.

If you're doing this on the JupyterHub, you already have all of the Python packages you need for this example, but we will need to update git-annex. The easiest way to do this is to install datalad-installer and then git annex using the following commands in your console:

```
  pip install datalad-installer
  datalad-installer git-annex
```

Next, this paper uses sklearn which has now changed to scikit-learn. To fix this, all we need to do is navigate to the repro-paper-sketch directory and find the requirements.txt file. In the requirements, change sklearn to scikit-learn and save it.

![sklearn](https://github.com/user-attachments/assets/d8d3e074-05a4-4ac5-aac4-513036e49885)


Lastly, this paper does not run unless you are using a "virtual environment". Do not get too bogged down with what that is, just follow the next steps. Also note, the first time you set up the virtual environment may take 5 or so minutes to load, so do not interrupt it!

```
  python -m venv myenv
  source myenv/bin/activate
```
If the virtual environment is activated, you will see the name of the environment at the beginning of each line in the console in parentheses: 

```
(myenv)joyvan...
```
Now, inside the repro-paper-sketch directory, you should be able to run the make command. Again, this may take a few minutes, especially when installing collected packages, so be patient! You will also likely get an error the first time, but we will fix that next.

```
  make
```

 If you're on JupyterHub (or if you don't have latexmk installed on your local system) you'll see something like:

 ```
  make: latexmk: No such file or directory
  make: *** [Makefile:12: main.pdf] Error 127
```
Oh no! We don't have `latexmk`, which is one of the requirements for this repo (https://github.com/datalad-handbook/repro-paper-sketch/blob/master/README.md#requirements). We don't need to install `latexmk`. Instead, let's change the `Makefile` and save it so that the `main.pdf` target (starting on line 10) looks the same as it does in the next panel. Leave the rest of the file alone. Please note: **The arrows are important! Tabbing or hitting space does not always work. Please copy and paste an arrow from one of the other sections in the makefile!**

![correct_makefile](https://github.com/user-attachments/assets/cb481d0b-a08c-4c9f-b678-1c332eebc567)


Whew! Now we can make the paper on JupyterHub, using `make clean` first to clean up any mess from the previous errors

```
  make clean
  make
```

This downloaded the [iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set), performed [KNN classification](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) on this dataset, embedded the results in publication LaTeX source files, and then compiled those source files into a publication pdf. To view the PDF double-click on main.pdf to see if everything looks correct. 

If it looks a little wonky, try running make one more time. If it still persists try the steps again or email us!

**Question 8**

 To the nearest two digits, what is the average weighted F1-score from **Table 1** in the PDF?

 - 0.88

 - 0.90

 - 0.92

 - 0.93


<details>
<summary>Click to see answer</summary>

 0.90
 
![Table1](https://github.com/user-attachments/assets/88651094-bdba-4849-acd5-520d3bdbd838)


***

</details>

**Question 9**

Let's say we want to update the appearance of the pairplot generated by the function `plot_relationships` in `code/mk_figuresnstats.py`. More specifically - we would like the context of the seaborn plot to be `paper`, the font to be scaled by `1.5`, the color palette to be `Dark2`, and the saved figure to have a resolution of `300` dpi. Once you have made your changes, close or delete the main.pdf and run `make` again to update the appearance of the plot.  In the space below insert the `plot_relationships` function with your modifications.

<details>
<summary>Click to see answer</summary>

```
def plot_relationships(df):
    """
    Create a pairplot to plot pairwise relationships in the dataset and save the
    results as png file
    :param df: pandas dataframe
    """
    sns.set_context("paper", font_scale=1.5)
    plot = sns.pairplot(df, hue='class', palette='Dark2')
    # save the figure as a png.
    plot.savefig('img/pairwise_relationships.png', dpi=300)
```
**BEFORE**

![original](https://github.com/user-attachments/assets/37931a0c-befb-49b7-afc3-e50579c892cc)

**AFTER**

![changed](https://github.com/user-attachments/assets/3d75c1bc-01eb-4c16-b1a4-3a9e220be7e2)



***

</details>

**Question 10**

Based on our difficulty building the paper with latexmk above, which of these elements  was missing from this reproducible paper?

-experimental data

-workflow

-execution environment

-results


<details>
<summary>Click to see answer</summary>

execution environment

***

</details>
