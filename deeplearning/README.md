# Deep Learning Labs Environments

First make sure you have a working **Python 3** [Conda distribution](https://anaconda.org/anaconda/python), then follow the next steps for you operative system. If your laptop features an nVidia GPU you can attempt a GPU install for better performance.

## Linux or Mac

### CPU environment

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-linux.yml) to your computer (right click -> Save link as...) and open a terminal in the same folder. Then type

    conda env create -f environment-linux.yml

to create an environment named `deeplearning-labs` with the necessary packages.

After creating the environment, open a terminal in the folder with the notebooks you want to work with. Then log into the environment running

    source activate deeplearning-labs

and then type

    jupyter notebook

to start the notebook server.

Note: if for any reason Jupyter is unable to find the environment (kernel) you just installed, you can configure it manually by running the following command in the terminal (after activating the environment):

    python -m ipykernel install --user --name deeplearning-labs --display-name "Python (deep-learning-labs)"

### GPU environment (only Linux, no Mac support for now)

Make sure you laptop has an nVidia GPU and the [appropriate drivers](http://www.nvidia.com//Download/index.aspx) for your operative system and GPU card. After that, download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-linux-gpu.yml) to your computer (right click -> Save link as...) and open a terminal in the same folder. Then type

    conda env create -f environment-linux-gpu.yml

and follow the same steps as for the CPU version. If you find issues when importing tensorflow or keras, you will need the find out what CUDA version is appropriate for your nVidia GPU and driver version, and modify the contents of the environment file to make use of an appropriate **cudatoolkit** version.

## Windows

### CPU environment

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-windows.yml) to your computer (right click -> Save link as...) and open an **Anaconda Navigator**. Click on the **Environments** tab, and look for the **Import** button. After clicking it, select as **Specification file** the environment file you downloaded. This will create an environment named `deeplearning-labs` with the necessary packages. Note the creation process might take a while.

After creating the environment, click the play icon at the environment name, and choose the option to launch a Jupyter notebook.

If for whatever reason the Jupyter notebook launch fails, you can also try opening an Anaconda Prompt in the folder with the notebooks you want to work with, then log into the environment running

    activate deeplearning-labs

and then type

    jupyter notebook

to start the notebook server.

### GPU environment

Make sure you laptop has an nVidia GPU and the [appropriate drivers](http://www.nvidia.com//Download/index.aspx) for your operative system and GPU card. After that, download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-windows-gpu.yml) (right click -> Save file as...) and follow the same steps as for the CPU version.

If you find issues when importing tensorflow or keras, you will need the find out what CUDA version is appropriate for your nVidia GPU and driver version, and modify the contents of the environment file to make use of an appropriate **cudatoolkit** version.

## Manual install

If after installing the environment you are unable to run keras or tensorflow, proceed as follows:

1. Remove the previously created conda environment (if any)

    conda env remove -n deeplearning-labs

2. Create the environment from scratch

    conda env create -n deeplearning-labs python=3.6

3. Log into the environment

    source activate deeplearning-labs       (Linux/Mac)
    activate deeplearning-labs              (Windows)

4. Manually install tensorflow. Try first to install the package via conda, and if the install fails for whatever reason, install with pip.

    conda install tensorflow
    pip install tensorflow

5. Manually install all the rest of packages in the corresponding environment file for you distribution. Again, try first to install the package via conda, and if the install fails for whatever reason, install with pip.

