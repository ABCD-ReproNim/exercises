# Week 3 Quiz

### Quiz Instructions

In this Week 3 Quiz, we will ask you a few questions about [ABCD Sampling, Recruitment, snf Retention](https://youtu.be/pvbRt5SntE8) and you will complete a few ReproNim exercises involving the [lecture on Containers and ReproEnv](https://youtu.be/UHw-DVgm-pE).

***

### ABCD (Sampling, Recruitment, Retention) Questions

First, we will ask you a few questions about ABCD Data.

**Question 1**

The ABCD sample is representative of youth in the United States.

- True
- False

<details>
<summary>Click to see answer</summary>

False

**Explanation**

- Due to the urban location of the sites and the self-selection of participants, the sample cannot be considered representative.  Additionally, hidden unmeasured variables may influence development and are not being accounted for.
- sources:
  - [Course video: Sampling, Recruitment, and Retention (31:18)](https://youtu.be/pvbRt5SntE8?t=2291)
  - [Recruiting the ABCD sample: Design considerations and procedures](https://www.sciencedirect.com/science/article/pii/S1878929317301809#sec0015)

***

</details>

**Question 2**

What was the primary method of recruitment for single birth children?

- Birth registries
- Mailing lists
- Schools
- Summer camps

<details>
<summary>Click to see answer</summary>

Schools

**Explanation**

- most 9-10 year olds are enrolled through school
- sources
  - [Course video: Sampling, Recruitment, and Retention (19:28)](https://youtu.be/pvbRt5SntE8?t=1168)
  - [Recruiting the ABCD sample: Design considerations and procedures](https://www.sciencedirect.com/science/article/pii/S1878929317301809#sec0025)

***

</details>

**Question 3**

What was the primary method of recruitment for twins?

- Birth registries
- Mailing lists
- Schools
- Summer camps

<details>
<summary>Click to see answer</summary>

Birth registries

**Explanation**

- twins are relatively rare requiring a more targeted strategy
  through birth registries.
- sources
  - [Course video: Sampling, Recruitment, and Retention (23:00)](https://youtu.be/pvbRt5SntE8?t=1380)
  - [Recruiting the ABCD sample: Design considerations and procedures](https://www.sciencedirect.com/science/article/pii/S1878929317301809#sec0055)

***

</details>

**Question 4**

What are two sources of sample bias the ABCD recruitment strategy could not account for due to constraints of the study?

- Urbanicity & Self-Selection
- Race & Sex
- Socio-Economic Status & Race
- Urbanicity & Sex
- Self-Selection & Socio-Economic Status

<details>
<summary>Click to see answer</summary>

Urbanicity & Self-Selection

**Explanation**

- self-selection
  - "it is well understood that self-selection by families into the study will likely be a major and unavoidable source of sampling bias" (Garavan et al. 2018).
  - source: [Recruiting the ABCD sample: Design considerations and procedures](https://www.sciencedirect.com/science/article/pii/S1878929317301809#sec0025)
- urbanicity
  - Most imaging centers are located in urban areas.
  - source: [Course video: Sampling, Recruitment, and Retention (14:02)](https://youtu.be/pvbRt5SntE8?t=842)

***

</details>

**Question 5**

How has the sociodemographic bias in missing assessments changed after the beginning of the COVID pandemic?

- Increased
- Stayed the same
- Decreased

<details>
<summary>Click to see answer</summary>

Decreased

**Explanation**

- It appears removing the burden of coming to lab reduces the
  sociodemographic bias
- source: [Course video: Sampling, Recruitment, and Retention (51:23)](https://youtu.be/pvbRt5SntE8?t=3083)

***

</details>

### ReproNim (Containers) Questions

Some of these questions are adapted, with modification, from the [Software Carpentries](http://software-carpentry.org) lesson on [Reproducible Computational Environments using Containers](https://carpentries-incubator.github.io/docker-introduction/index.html), which is licensed under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode). Other questions were adapted, with modification, from the [Neurohackweek](http://neurohackweek.github.io/) lesson on [Docker for Scientists](https://neurohackweek.github.io/docker-for-scientists/), which is licensed under the [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/legalcode).

The following questions require Docker to be installed on your computer. Please [download Docker](https://www.docker.com/products/docker-desktop) and then follow the installation instructions.

**Question 6**

Once Docker is installed, try downloading and running the alpine Docker container. Which of the following terminal commands would download and run the alpine Docker container? (Select all that apply)

- [ ] `docker run alpine`
- [ ] `docker image alpine`
- [ ] `docker pull alpine; docker run alpine`
- [ ] `docker build alpine`

<details>
<summary>Click to see answer</summary>

- [x] `docker run alpine`
- [ ] `docker image alpine`
- [x] `docker pull alpine; docker run alpine`
- [ ] `docker build alpine`

***

</details>

**Question 7**

The alpine docker image is a minimal image based on Alpine Linux. It is designed for you to provide commands yourself as arguments to the docker run command. For example the command `docker run alpine echo 'Hello World'` would pass the `echo 'Hello World'` command to the alpine container. Try it out. In Alpine Linux, the operating system version information is stored in a file located at `/etc/alpine-release`. Use this information to find the exact Alpine Linux version number for the alpine docker image with tag `3.14`. Hint: be sure to use the tag `3.14` in all docker pull and run commands that you use to answer this question.

- 3.14.2
- 3.14.3
- 3.14.4
- 3.14.5

<details>
<summary>Click to see answer</summary>

3.14.3

**Explanation**
Use the command `docker run alpine:3.14 cat /etc/alpine-release` to get the version information.

***

</details>

**Question 8**

8) Use docker commands to download the `bids/base_fsl` image [from Docker Hub](https://hub.docker.com/r/bids/base_fsl/). Also download [this map from NeuroVault.org](http://neurovault.org/media/images/457/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz) and place it in an example folder in your current working directory. Using the `-v` option as described in the lecture (or “volume flags” if you are referencing [the Docker documentation](https://docs.docker.com/storage/volumes/)), mount your folder so that it will be accessible from the container when you run it. Now use the `fslstats` command to output the mean entropy of non-zero voxels for the image you downloaded. Hint: Use `fslstats --help` to determine the option that will return the mean entropy of non-zero voxels. What is the mean entropy of the non-zero voxels in the downloaded image?

- 0.410776
- 0.929105
- 0.405803
- 0.914086

<details>
<summary>Click to see answer</summary>

0.914086

**Explanation**
Assuming you have downloaded the required data file in a directory called `data` within your current directory, you would run your Docker image using
```
docker run -ti --rm -v $(pwd)/data:/data bids/base_fsl
```
Within this docker image, you can run the command
```
fslstats data/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz -E
```
to get the correct answer.

***

</details>

**Question 9**

Next, we'll smooth the downloaded image using a Gaussian kernel with the FSL command `fslmaths /data/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz -kernel gauss 10 -fmean /data/smoothed.nii.gz`. Confirm that this command, which you issued inside of the Docker container, added the `smoothed.nii.gz` output file to the example folder on your host system. Use the same commands as before to calculate the mean entropy of the nonzero voxels in the smoothed image. What is it?

- 0.705882
- 0.701026
- 0.694043
- 0.698877

<details>
<summary>Click to see answer</summary>

0.705882

***

</details>

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

Build this docker image by navigating to the same directory as your Dockerfile and running `docker build -t my_custom_fsl .` Don't forget about the dot at the end, which tells Docker where to find the Dockerfile. Next register for an account on Docker Hub. Log into Docker Hub in your console using `docker login`. Build your image with the name `<username>/my_custom_fsl` and push your image to Docker Hub using `docker push <username>/my_custom_fsl.` Find a link to your image online on Docker Hub. There's no right or wrong answer for this one. Simply take a moment to reflect on your accomplishments.

**Question 11**

Extra credit (not graded). Using NeuroDocker, create a Dockerfile that will produce an image with FSL that answers Question #8 above. You will need to install FSL, download the image file using a strategy similar to the one used [here](https://github.com/ReproNim/neurodocker#minimize-existing-docker-image), and set the entry-point to use the command that you used to answer question #8. In the text box below, enter the lines that you would use to create this Dockerfile using NeuroDocker. Note: you do not need to actually build this Docker image, which could take quite some time depending on your internet connection. After doing this, you will have built a container to reproducibly answer our quiz question. Think about how you could use the same tools to create reproducible analysis pipelines for your own research.

<details>
<summary>Click to expand and see one potential answer</summary>

```
download_cmd="mkdir /data && curl -sSL -o /data/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz http://neurovault.org/media/images/457/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz"

docker run --rm repronim/neurodocker generate docker --base debian:stretch --pkg-manager apt --fsl version=6.0.3 --run="$download_cmd" --entrypoint "fslstats /data/tfMRI_SOCIAL_TOM-RANDOM_zstat1.nii.gz -E" > Dockerfile
```

</details>
