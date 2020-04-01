
# Installing Tarski

## Software Requirements
Tarski is mostly developed in Python, and requires a working Python>=3.6 installation.
We strongly recommend installing Tarski within a Python
[virtual environment](https://docs.python.org/3/tutorial/venv.html).
The installation instructions below will install for you any additional
required dependencies.


## Installation Instructions

You can install the latest Tarski release with:

    pip install tarski

If instead you want to use the latest code available on the Github repository, 
you can install with:
    
    pip install -U git+https://github.com/aig-upf/tarski.git


## Installing Tarski in Development Mode
If developing Tarski, we recommend cloning from the Github repository and doing
a development installation (the`-e` flag for `pip`):
    
    git clone https://github.com/aig-upf/tarski
    cd tarski
    pip install -e .

This will install the project in "editable mode", meaning that any modification
to the files is immediately reflected in the _installed_ library.

## Installing Extras (Experimental)
Tarski allows the _optional_ installation of certain extras that will allow you
to run certain non-essential functionalities of the library. For instance,
the `tarski.sdd` experimental package allows you to interact with the
[PySDD package](https://github.com/wannesm/PySDD) for sentential decision diagrams
in order to analyze the structure of action schema preconditions. To use this
`tarski.sdd` optional package, you'd need to pip install with the `sdd` "extra",
as in: 

    pip install tarski[sdd]

We strongly recommend to use these extras only if you know what you're doing.
Current extras include:

* `arithmetic`: Enables use of Tarski for dealing with numeric planning problems, algebraic matrix sorts, etc.
               Installs `scipy` and `numpy` python packages.
* `sdd`: SDD-based analysis of action schemas (might require additional manual installation steps).
* `rddl`: Enables dealing with RDDL probabilistic problems. Installs `pyrddl` python package.