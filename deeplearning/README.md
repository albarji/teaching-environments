# Deep Learning Labs Environments

To prepare your environment for running these labs it is recommended that you build a conda environment. First make sure you have a working [Conda distribution](https://anaconda.org/anaconda/python), then follow the next steps for you operative system. If your laptop features an nVidia GPU you can attemt a GPU install for better performance.

## Linux and Mac 

### CPU environment

Open a terminal in this folder and run

    conda env create -f environment-linux.yml

to create an environment named `deeplearning-labs` with the necessary packages. Then log into the environment running

    source activate deeplearning-labs

The environment includes jupyter notebooks, so you just need to type

    jupyter notebook

to start the notebook server.

## GPU environment

Make sure you laptop has an nVidia GPU and the [appropriate drivers](www.nvidia.com/Download/index.aspx) for your operative system and GPU card. Then open a terinal in this folder and run 

    conda env create -f environment-linux-gpu.yml

and follow the same steps as for the CPU version. If you find issues when importing tensorflow or keras, install the latest [nVidia Toolkit](https://developer.nvidia.com/cuda-toolkit) and repeat the steps.

## Windows

TODO


## Manual install

If after installing the environment you are unable to run keras or tensorflow, proceed as follows:

* Remove the previously created conda environment

    conda env remove -n deeplearning-labs

* Create the environment from scratch

    conda env create -n deeplearning-labs python=3.6

* Log into the environment

    source activate deeplearning-labs

* Manually install tensorflow. Try first to install the package via conda, and if the install fails for whatever reason, install with pip.

    conda install tensorflow
    pip install tensorflow

* Manually install all the rest of packages in the corresponding environment file for you distribution. Again, try first to install the package via conda, and if the install fails for whatever reason, install with pip.

