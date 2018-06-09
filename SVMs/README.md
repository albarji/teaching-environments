# Support Vector Machines Labs Environments

First make sure you have a working **Python 3** [Conda distribution](https://anaconda.org/anaconda/python), then follow the next steps for you operative system.

## Linux or Mac

Download the [environment file](environment-linux.yml) to your computer and open a terminal in the same folder. Then type

    conda env create -f environment-linux.yml

to create an environment named `svm-labs` with the necessary packages. Then log into the environment running

    source activate deeplearning-labs

The environment includes jupyter notebooks, so you just need to type

    jupyter notebook

to start the notebook server.

## Windows

Download the [environment file](environment-windows.yml) to your computer and open an **Anaconda Prompt** terminal in the same folder. Then type

    conda env create -f environment-windows.yml

to create an environment named `deeplearning-labs` with the necessary packages. Then open **Anaconda Navigator**, look for this environment and launch a Jupyter notebook.


