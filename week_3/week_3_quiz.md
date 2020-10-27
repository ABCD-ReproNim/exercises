# Week 3 Quiz

### Quiz Instructions

In this Week 3 Quiz, we will ask you a few questions about ABCD (Sampling, Recruitment, Retention) and you will complete a few ReproNim exercises (Containers and ReproEnv).

***

### ABCD (Sampling, Recruitment, Retention) Questions

First, we will ask you a few questions about ABCD Data.

**Question 1**

The ABCD sample is representative of youth in the United States.

<input type="radio" name="q1"> True <br>
<input type="radio" name="q1"> False

**Question 2**

What was the primary method of recruitment for single birth children?

<input type="radio" name="q2"> Birth registries <br>
<input type="radio" name="q2"> Mailing lists <br>
<input type="radio" name="q2"> Schools <br>
<input type="radio" name="q2"> Summer camps

**Question 3**

What was the primary method of recruitment for twins?

<input type="radio" name="q3"> Birth registries <br>
<input type="radio" name="q3"> Mailing lists <br>
<input type="radio" name="q3"> Schools <br>
<input type="radio" name="q3"> Summer camps

**Question 4**

What are two sources of sample bias the ABCD recruitment strategy could not account for due to constraints of the study?

<input type="radio" name="q4"> Urbanicity & Self-Selection <br>
<input type="radio" name="q4"> Race & Sex <br>
<input type="radio" name="q4"> Socio-Economic Status & Race <br>
<input type="radio" name="q4"> Urbanicity & Sex <br>
<input type="radio" name="q4"> Self-Selection & Socio-Economic Status

**Question 5**

How has the sociodemographic bias in missing assessments changed after the beginning of the COVID pandemic?

<input type="radio" name="q5"> Increased <br>
<input type="radio" name="q5"> Stayed the same <br>
<input type="radio" name="q5"> Decreased

### ReproNim (Containers) Questions

Some of these questions are adapted, with modification, from the [Software Carpentries](http://software-carpentry.org) lesson on [Reproducible Computational Environments using Containers](https://carpentries-incubator.github.io/docker-introduction/index.html), which is licensed under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode). Other questions were adapted, with modification, from the [Neurohackweek](http://neurohackweek.github.io/) lesson on [Docker for Scientists](https://neurohackweek.github.io/docker-for-scientists/), which is licensed under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode).

The following questions require Docker to be installed on your computer. Please [download Docker](https://www.docker.com/products/docker-desktop) and then follow the installation instructions.

**Question 6**

Once Docker is installed, try downloading and running the alpine Docker container. Which of the following terminal commands would download and run the alpine Docker container? (Select all that apply)

- [ ] `docker run alpine`
- [ ] `docker image alpine`
- [ ] `docker pull alpine; docker run alpine`
- [ ] `docker build alpine`

**Question 7**

The alpine docker image is a minimal image based on Alpine Linux. It is designed for you to provide commands yourself as arguments to the docker run command. For example the command `docker run alpine echo 'Hello World'` would pass the `echo 'Hello World'` command to the alpine container. Try it out. In Alpine Linux, the operating system version information is stored in a file located at `/etc/os-release`. Use this information to find the exact Alpine Linux version number for the alpine docker image with tag `3.11`. Hint: be sure to use the tag `3.11` in all docker pull and run commands that you use to answer this question.

<input type="radio" name="q7"> 3.11.4 <br>
<input type="radio" name="q7"> 3.11.5 <br>
<input type="radio" name="q7"> 3.11.6 <br>
<input type="radio" name="q7"> 3.11.7

**Question 8**

8) Use docker commands to download the `bids/base_fsl` image [from Docker Hub](https://hub.docker.com/r/bids/base_fsl/). Also download [this map from NeuroVault.org](http://neurovault.org/media/images/457/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz) and place it in an example folder in your current working directory. Using the `-v` option as described in the lecture (or “volume flags” if you are referencing [the Docker documentation](https://docs.docker.com/storage/volumes/)), mount your folder so that it will be accessible from the container when you run it. Now use the `fslstats` command to output the mean entropy of non-zero voxels for the image you downloaded. Hint: Use `fslstats --help` to determine the option that will return the mean entropy of non-zero voxels. What is the mean entropy of the non-zero voxels in the downloaded image?

<input type="radio" name="q8"> 0.410776 <br>
<input type="radio" name="q8"> 0.929105 <br>
<input type="radio" name="q8"> 0.405803 <br>
<input type="radio" name="q8"> 0.914086

**Question 9**

Next, we'll smooth the downloaded image using a Gaussian kernel with the FSL command `fslmaths /data/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz -kernel gauss 10 -fmean /data/smoothed.nii.gz`. Confirm that this command, which you issued inside of the Docker container, added the `smoothed.nii.gz` output file to the example folder on your host system. Use the same commands as before to calculate the mean entropy of the nonzero voxels in the smoothed image. What is it?

<input type="radio" name="q9"> 0.705882 <br>
<input type="radio" name="q9"> 0.701026 <br>
<input type="radio" name="q9"> 0.694043 <br>
<input type="radio" name="q9"> 0.698877

**Question 10**

Now we will use the aforesaid `bids/base_fsl` image as a base image for a custom Docker image. Using your favorite editor, save a new file called Dockerfile inside an empty folder. The first line of this file should be:

```
FROM bids/base_fsl
```

In the next lines in your Dockerfile, download your favorite scientific computing software. For example, if you wanted to add python, your Dockerfile could look like:

```
FROM bids/base_fsl
RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /opt/miniconda.sh
RUN /bin/bash /opt/miniconda.sh -b -p /opt/conda
ENV PATH="/opt/conda/bin:$PATH"
```

Build this docker image by navigating to the same directory as your Dockerfile and running `docker build -t my_custom_fsl .` Don't forget about the dot at the end, which tells Docker where to find the Dockerfile. Next register for an account on Docker Hub. Log into Docker Hub in your console using `docker login`. Build your image with the name `<username>/my_custom_fsl` and push your image to Docker Hub using `docker push <username>/my_custom_fsl.` Find a link to your image on Docker Hub and ~~paste below~~ (in responsive versions of this quiz, you would be asked to submit the link for grading. Here, simply take a moment to reflect on your accomplishments).

**Question 11**

Extra credit (not graded). Using NeuroDocker, create a Dockerfile that will produce an image with FSL that answers Question #8 above. You will need to install FSL, download the image file using a strategy similar to the one used [here](https://github.com/ReproNim/neurodocker#minimize-existing-docker-image), and set the entry-point to use the command that you used to answer question #8. In the text box below, enter the lines that you would use to create this Dockerfile using NeuroDocker. Note: you do not need to actually build this Docker image, which could take quite some time depending on your internet connection. After doing this, you will have built a container to reproducibly answer our quiz question. Think about how you could use the same tools to create reproducible analysis pipelines for your research.

<details>
<summary>Click to expand and see one potential answer</summary>

```
download_cmd="mkdir /data && curl -sSL -o /data/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz http://neurovault.org/media/images/457/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz"

docker run --rm repronim/neurodocker generate docker --base debian:stretch --pkg-manager apt --fsl version=6.0.3 --run="$download_cmd" --entrypoint "fslstats /data/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz -E" > Dockerfile
```

</details>
