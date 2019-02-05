
# Tarski - The Planning Problem Definition Module [![Build Status](https://travis-ci.com/aig-upf/tarski.svg?branch=master)](https://travis-ci.com/aig-upf/tarski)

## What is Tarski
To be defined :-)

## Installation and Usage

You can install Tarski through pip by issuing the following on the root directory of the project: 
    
    pip install -e 

If you are developing Tarski, we recommend using a virtual environment and installing in development mode
by using the `-e` flag:  

    pip install -e .

This will install the project in "editable mode", i.e., by using the actual files from the project directory
tree, as opposed to a copy installed in some system /virtualenv directory. Any modification to the files
will thus be immediately reflected in the _installed_ library.


## Testing 
All of Tarski's tests live under the `tests` directory (shocking!).
To run them, you will need `pytest` (`pip install pytest`). Just run on the root directory:

    pytest





## Software Requirements
Tarski requires Python >= 3.5.
The above installation instructions will install under the hood a number of dependencies, among which
numpy and scipy.


### Supported Languages
At the moment, Tarski supports the following modeling languages:
* PDDL
* Functional STRIPS


## Modules

* Description Logic (`tarski.dl`)
