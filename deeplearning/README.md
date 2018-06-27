# Deep Learning Labs Environments

First make sure you have a working **Python 3** [Conda distribution](https://anaconda.org/anaconda/python), then follow the next steps for you operative system. If your laptop features an nVidia GPU you can attempt a GPU install for better performance.

## Linux or Mac

### CPU environment

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-linux.yml) to your computer and open a terminal in the same folder. Then type

    conda env create -f environment-linux.yml

to create an environment named `deeplearning-labs` with the necessary packages.

After creating the environment, open a terminal in the folder with the notebooks you want to work with. Then log into the environment running

    source activate deeplearning-labs

and then type

    jupyter notebook

to start the notebook server.

### GPU environment

Make sure you laptop has an nVidia GPU and the [appropriate drivers](www.nvidia.com/Download/index.aspx) for your operative system and GPU card. After that, download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-linux-gpu.yml) to your computer and open a terminal in the same folder. Then type

    conda env create -f environment-linux-gpu.yml

and follow the same steps as for the CPU version. If you find issues when importing tensorflow or keras, install the latest [nVidia Toolkit](https://developer.nvidia.com/cuda-toolkit) and repeat the steps.

## Windows

### CPU environment

Download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-windows.yml) to your computer and open an **Anaconda Prompt** terminal in the same folder. Then type

    conda env create -f environment-windows.yml

to create an environment named `deeplearning-labs` with the necessary packages. 

After creating the environment, open **Anaconda Navigator**, look for this environment and launch a Jupyter notebook. If for whatever reason this fails, you can also try opening a terminal in the folder with the notebooks you want to work with, then log into the environment running

    activate deeplearning-labs

and then type

    jupyter notebook

to start the notebook server.

### GPU environment

Make sure you laptop has an nVidia GPU and the [appropriate drivers](www.nvidia.com/Download/index.aspx) for your operative system and GPU card. After that, download the [environment file](https://raw.githubusercontent.com/albarji/teaching-environments/master/deeplearning/environment-windows-gpu.yml) and open an **Anaconda Prompt** terminal in the same folder. Then type

    conda env create -f environment-windows-gpu.yml

and follow the same steps as for the CPU version. If you find issues when importing tensorflow or keras, install the latest [nVidia Toolkit](https://developer.nvidia.com/cuda-toolkit) and repeat the steps.

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

