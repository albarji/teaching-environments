# Support Vector Machines Labs Environments

First make sure you have a working **Python 3** [Conda distribution](https://anaconda.org/anaconda/python), then follow the next steps for you operative system.

## Linux or Mac

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/SVMs/environment-linux.yml) to your computer and open a terminal in the same folder. Then type

    conda env create -f environment-linux.yml

to create an environment named `svm-labs` with the necessary packages.

After creating the environment, open a terminal in the folder with the notebooks you want to work with. Then log into the environment running

    source activate svm-labs

and then type

    jupyter notebook

to start the notebook server.

## Windows

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/SVMs/environment-windows.yml) to your computer and open an **Anaconda Prompt** terminal in the same folder. Then type

    conda env create -f environment-windows.yml

to create an environment named `svm-labs` with the necessary packages. 

After creating the environment, open **Anaconda Navigator**, look for this environment and launch a Jupyter notebook. If for whatever reason this fails, you can also try opening a terminal in the folder with the notebooks you want to work with, then log into the environment running

    activate svm-labs

and then type

    jupyter notebook

to start the notebook server.
