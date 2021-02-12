# Week 11 Quiz

### Quiz Instructions

In this Week 11 Quiz, we will ask you a few questions about [Visualizing ABCD data and the ReproPub re-executable paper](https://abcd-repronim.github.io/materials/week-11/). We also encourage you to fork the [repo](https://github.com/62442katieb/NH19-Visualization/blob/binder-live/) Katie Bottenhorn used as a demo for her lecture
and play around with the various plots that are generated. 

***


**Question 1**

The lecture and [ReproPub preprint](https://zenodo.org/record/3336609#.X3IzuNNKjOQ) point to [Ghosh et al's 2017 "simple, re-executable neuroimaging publication"](https://f1000research.com/articles/6-124
) as a proof of concept of the ReproPub. In this question, we will see if this paper is indeed re-executable. First, create a new directory for the output

```bash
mkdir -p week_11/problem_1/output
cd week_11/problem_1
```

Now, rerun the paper's analysis using the provided docker commands provided in the paper:
```
docker run -it --rm -v $(pwd)/output:/opt/repronim/simple_workflow/scripts/output repronim/simple_workflow:1.1.0 run_demo_workflow.py --key 11an55u9t2TAf0EV2pHN0vOd8Ww2Gie-tHp9xGULh_dA
```

If you would like to run this command on the JupyterHub, [please see these instructions](https://github.com/ReproNim/simple_workflow/blob/master/README.md#4-other-containers) to use Singularity instead of Docker.

This will take a while to run (e.g. a couple hours). Feel free to work on some of the other problems while you're waiting. Or you can watch a [panda cam](https://nationalzoo.si.edu/webcams/panda-cam) to pass the time. The possibilities are endless!

Once the simple workflow is done, use the paper's supplied `check_output.py` program to verify that your results match the original results.

```
docker run -it --rm -v $(pwd)/output:/opt/repronim/simple_workflow/scripts/output repronim/simple_workflow:1.1.0 check_output.py
```

Based on the output of this program, what was the **ORIGINAL** platform on which the paper's analysis was performs

- platform: Linux-4.9.19-moby-x86_64-with-debian-8.7, FSL version: 5.0.9
- platform: Linux-4.9.19-moby-x86_64-with-debian-8.7, FSL version: 6.0
- platform: Linux-4.19.121-linuxkit-x86_64-with-debian-8.8, FSL version: 5.0.9
- platform: Linux-4.19.121-linuxkit-x86_64-with-debian-8.8, FSL version: 6.0

<details>
<summary>Click to see answer</summary>

platform: Linux-4.9.19-moby-x86_64-with-debian-8.7
FSL version: 5.0.9
***

</details>

Great, we have re-executed the "simple publication." That is, we ran the same analysis on the same data using the same computational environment.

**Question 2**

Next we'll look at running different analysis on the same data using a different reproducible paper example. It may not surprise you to learn that DataLad can help you write a fully reproducible paper. You can read more about this [in the DataLad handbook](http://handbook.datalad.org/en/latest/usecases/reproducible-paper.html). We will use the DataLad ["Automatically Reproducible Paper Template"](https://github.com/datalad-handbook/repro-paper-sketch/). The next two questions help you explore how to do this.

From the `week_11` directory that you created for problem #1, clone the reproducible paper repository:

```
datalad clone https://github.com/datalad-handbook/repro-paper-sketch.git
```

If you're doing this on the JupyterHub, you already have all of the Python packages you need for this example. If you're not on the JupyterHub, you should [follow the instructions in the repository's `README.md`](https://github.com/datalad-handbook/repro-paper-sketch/blob/master/README.md#how-to-use-this-template) file, which indicate that you should create a virtual environment using `virtualenv`. You can follow those instructions or use the next few lines, which will create a conda environment instead

```
conda create --name repro-paper-sketch python=3.8 --no-default-packages
# follow prompts to create the conda environment
source activate repro-paper-sketch
cd repro-paper-sketch
pip install -r requirements.txt
```

Now, let's run

```
make
```

to generate the reproducible paper. If you're on JupyterHub (or if you don't have `latexmk` installed on your local system) you'll see something like

```
...
latexmk -pdf -g main.tex
make: latexmk: No such file or directory
make: *** [Makefile:7: main.pdf] Error 127
```

Oh no! We don't have `latexmk`, which is one of the [requirements for this repo](https://github.com/datalad-handbook/repro-paper-sketch/blob/master/README.md#requirements). We don't need to install `latexmk`. Instead, let's change the `Makefile` using your favorite text editor (e.g. `nano Makefile` on the JupyterHub) so that the `main.pdf` target (on line 6) reads:

```
main.pdf: main.tex references.bib results_def.tex
    pdflatex $<
    bibtex $(basename $<)
    pdflatex $<
    pdflatex $<
```

Whew! Now we can make the paper on JupyterHub, using `make clean` first to clean up any mess from the previous errors

```
make clean
make
```

This downloaded the [iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set), performed [KNN classification](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) on this dataset, embedded the results in publication LaTeX source files, and then compiled those source files into a publication pdf. Inspecting Table 1 of `main.pdf` (or the output in `prediction_report.csv`), we can see that the KNN classifier achieved a weighted average F1 score of 0.90 on the test set.

Now suppose that instead of re-executing this paper, we wish to augment the analysis while keeping the data the same. Suppose we have a hunch that the classification algorithm might benefit from scaling the input data first.

(Don't worry if Python isn't your primary language or if you're not used to classification algorithms. You can copy paste the code below. The objective of this problem set is to learn about reproducible publications)

So we edit the Python code in `code/mk_figuresnstats.py`. On line 13, after the import statements, add

```
from sklearn.preprocessing import MinMaxScaler
```

and then around line 59, we add

```
    # Scale the feature matrix before classification
    scaler = MinMaxScaler()
    # Scaler parameters are learned only from the training set
    X_train = scaler.fit_transform(X_train)
    # And then applied to the test set as well (no peaking!)
    X_test = scaler.transform(X_test)
    
    # Fit the model and make predictions on the test dataset
    knn = ...
```

The last two lines are there for context so that you see where to add the `scaler` lines. Save the file and return to the shell.

We changed the analysis code. Now we can rerun the entire study with

```
make
```

Before we look at the results, let's be good reproducibility advocates and document our changes. First, we'll remind ourselves what we changed:

```
$ datalad status
...
    modified: Makefile (file)
    modified: code/mk_figuresnstats.py (file)
    modified: prediction_report.csv (file)
```

Oh yeah, we changed the Makefile to build the pdf without `latexmk`. Let's note that first.

```
datalad save -m "Use pdflatex explicitly instead of latexmk in Makefile so that we can build the paper on JupyterHub" Makefile
```

And we also add feature scaling to the analysis code.

```
datalad save -m "Use MinMaxScaler to scale features before classification." code/mk_figuresnstats.py prediction_report.csv
```

Great, now let's inspect the compiled paper (or `prediction_report.csv`) to see if scaling the feature had any effect. To the nearest two digits, what is the new average weighted F1-score?

- 0.88
- 0.90
- 0.92
- 0.93

<details>
<summary>Click to see answer</summary>

0.93
***

</details>

**Question 3** 

Let's say we want to update the appearance of the pairplot generated by the function `plot_relationships` in 
`code/mk_figuresnstats.py`. More specifically - we would like the context of the seaborn plot to be `paper`, 
the font to be scaled by 1.5, the color palette to be `Dark2`, and the saved figure to have a resolution of 300 dpi. 

Since we changed the code used to generate the figure, we will now run `make` again to update the appearance of the 
plot. We will once again save the changes that we have made to the script with `datalad save -m "changed appearance of the pairplot" code/mk_figuresnstats.py`. 

In the space below insert the `plot_relationships` function with your modifications. 

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
***

</details>

**Question 4**

Based on our difficulty building the paper with `latexmk` above, which of the four required elements of the ReproPub is the DataLad "repro-paper-sketch" missing?

- experimental data
- workflow
- execution environment
- results

<details>
<summary>Click to see answer</summary>

Execution environment. We had to either install latexmk or change the Makefile.
***

</details>

**Question 5** 

We also learned about [Nilearn] in the ABCD lecture, and we can use it to visualize the segmentations we created in week 9. 

Once you have completed the [week 9 quiz](https://github.com/ABCD-ReproNim/exercises/blob/main/week_9/week_9_quiz.md#repronim-questions), you should use the following commands to clone the dataset and get the contents that were generated in the `derivatives` folder. 
We will also create two new folders to store the code and the figures that we will generate. 

- `datalad clone week9_analysis week11_analysis`
- `cd week11_analysis`
- `datalad get derivatives`
- `mkdir code derivatives`

Next, we're going to create a python script that will use Nilearn to create two figures corresponding to the `fast` 
and `none` parameters. These figures will have a resolution of 300 dpi. Place this script in the `code` folder.

```
import nibabel as nib
import pandas as pd
from glob import glob
from nilearn import plotting

for ____ in glob('____/sub-*'):
    ____ = ____.split("/")[-1]
    for ____ in ["none", "fast"]:
        seg_img = nib.load(f'../derivatives/first/{participant}/{parameter}_all_{parameter}_firstseg.nii.gz')
        title = f'{participant}; method: {____}'
        p = ____.plot_roi(____, title=title) 
        p.savefig(f'../figures/{participant}_fsl-{parameter}_hippocampus.png', dpi=__)
```

How would you run this script such that an informative commit message is associated with the run? 

<details>
<summary>Click to see answer</summary>

Python script solution:
```
import nibabel as nib
import pandas as pd
from glob import glob
from nilearn import plotting

for participant in glob('../derivatives/first/sub-*'):
    participant = participant.split("/")[-1]
    for parameter in ["none", "fast"]:
        seg_img = nib.load(f'../derivatives/first/{participant}/{parameter}_all_{parameter}_firstseg.nii.gz')
        title = f'{participant}; method: {parameter}'
        p = plotting.plot_roi(seg_img, title=title) 
        p.savefig(f'../figures/{participant}_fsl-{parameter}_hippocampus.png', dpi=300)
```

Datalad run command: 
```
datalad run -m "generating plots of hippocampus segmentations" --output "../figures/*" "python ./generate_figs.py"
```
***

</details>


**Question 6**

It is nice that "repro-paper-sketch" build our LaTeX source for us, but this isn't a requirement of the ReproPub. To create a ReproPub, we need only recognize that the experimental data, workflow, execution environment, and results are themselves research objects and track their provenance. Luckily, if you completed the Week 9 ReproNim quiz, you already have a research finding with provenance tracking, namely you determined that hippocampal volume measurements in the [Study Forrest dataset](https://github.com/psychoinformatics-de/studyforrest-data-structural) were not robust to the two methods of FSL [FIRST](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST) that you tried. Let's suppose that you now want to share this groundbreaking research finding in a reproducible publication.

The `week11_analysis` DataLad dataset contains the provenance for our

- experimental data (using the previous `datalad clone` and `datalad get` commands),
- workflow (using the previous and current `datalad run` commands,
- computational environment (using the previous `datalad container-add` and `datalad containers-run` commands), and
- results (in the `hippocampal_volume.tsv` file that was created and tracked as a result of a previous `datalad run` command
as well as the figures that we just generated in question 4).

If you haven't already done so, create a GitHub personal access token by going to <https://github.com/settings/tokens/new>, creating a token with "repo," "user," and "workflow" scope, and saving the token to your clipboard or some place more permanent. You'll use that token in the following command

```
git config --global --add hub.oauthtoken <insert token here>
```

Next, reorder the commands below to create a tag for our dataset (to mark this specific version as the one we'll use for our seminal research paper), push your dataset to GitHub, and push the tag we created to GitHub. See the [DataLad handbook if you need some help](http://handbook.datalad.org/en/latest/basics/101-130-yodaproject.html?highlight=GitHub#publishing-the-dataset-to-github):

- `datalad create-sibling-github -d . repro-paper-hippocampal-volumes`
- `datalad save -m "Add paper tag" --version-tag repro-paper`
- `git push github --tags`
- `datalad push --to github`

<details>
<summary>Click to see answer</summary>
Here is one possible solution:
```
datalad create-sibling-github -d . repro-paper-hippocampal-volumes
datalad push --to github
datalad save -m "Add paper tag" --version-tag repro-paper
git push github --tags
```

However, the `datalad save` command could be done at any point before the `git push` command.

***

</details>

**Question 7**

You have successfully pushed your reproducible paper elements to a repository on GitHub. The last step is to create a DOI for this resource. Create an account on zenodo.org, link it with your GitHub account, and enable the `repro-paper-hippocampal-volumes` repository that you just created. Then create a new release from the `repro-paper` tag that you created in the previous step. If you've done these steps correctly, you should have published a DOI on zenodo.org. Paste your new DOI in the text box below. When you are writing your groundbreaking paper, you can refer to this DOI to reference your DataLad dataset.

**Question 8**

Matplotlib is built on top of Seaborn. 

- True
- False 

<details>
<summary>Click to see answer</summary>

- False 

Explanation: It's the other way around; Seaborn abstracts away some of Matplotlib's complexities and provides an easier to use API. 