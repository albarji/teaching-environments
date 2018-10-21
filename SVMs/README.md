# Support Vector Machines Labs Environments

First make sure you have a working **Python 3** [Conda distribution](https://anaconda.org/anaconda/python), then follow the next steps for you operative system.

## Linux or Mac

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/SVMs/environment-linux.yml) to your computer (right click -> Save link as...) and open a terminal in the same folder. Then type

    conda env create -f environment-linux.yml

to create an environment named `svm-labs` with the necessary packages.

After creating the environment, open a terminal in the folder with the notebooks you want to work with. Then log into the environment running

    source activate svm-labs

and then type

    jupyter notebook

to start the notebook server.

## Windows

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/SVMs/environment-windows.yml) to your computer (right click -> Save link as...) and open an **Anaconda Navigator**. Click on the **Environments** tab, and look for the **Import** button. After clicking it, select as **Specification file** the environment file you downloaded. This will create an environment named `svm-labs` with the necessary packages. Note the creation process might take a while.

After creating the environment, click the play icon at the environment name, and choose the option to launch a Jupyter notebook.

If for whatever reason the Jupyter notebook launch fails, you can also try opening an Anaconda Prompt in the folder with the notebooks you want to work with, then log into the environment running

    activate svm-labs

and then type

    jupyter notebook

to start the notebook server.
