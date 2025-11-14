## Creating and using a local Jupyter Hub

All students can get the same environment locally via docker, including the ability to use singularity within the docker container. For installing docker see [Docker](https://docs.docker.com/desktop/).

Open a terminal on your computer. Copy and paste the following:

```bash
mkdir -p abcd-repronim
docker run -it --rm --privileged -p 8888:8888 -v $(pwd)/abcd-repronim:/home/jovyan \
  satra/abcd-repronim:latest start.sh jupyter lab
```

When this initializes you will notice an output that ends with http://127.0.0.1:8888/?token=43ea5391332129e84e6e87566089c88e429afe20a62d15fe (the token will be different each time you start). Paste this in your browser to access jupyterlab. 
This is the same interface that we are using in the online version, and it should contain everything that you need.

Once you are done using your local hub, you can hit Ctrl+C in the terminal you ran the docker in and then y for yes to close down the session. if you have mounted the directory in the docker command and saved notebooks and files in the lab, your information will be preserved.
The abcd-repronim directory will be mounted inside and will preserve any changes you make in your home directory. The above command uses the full path. This is necessary.
The --privileged flag is necessary if you want to run singularity inside the container.

We have also put all this into a short video for you:
