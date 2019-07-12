
# Tarski - The Planning Problem Definition Module [![Build Status](https://travis-ci.com/aig-upf/tarski.svg?branch=master)](https://travis-ci.com/aig-upf/tarski)

## What is Tarski
Tarski is a parser and preprocessor to create, manipulate and transform 
[AI planning](https://en.wikipedia.org/wiki/Automated_planning_and_scheduling) problems. 


## Installation

You can install the latest official Tarski release with

    pip install tarski

If instead you want to use the latest code available on the Github repository, use 
    
    pip install -U git+https://github.com/aig-upf/tarski.git


## Development
If developing Tarski, we recommend cloning from the Github repository and doing a development installation
(`pip`'s `-e` flag) on a [virtual environment](https://docs.python.org/3/tutorial/venv.html):
    
    git clone https://github.com/aig-upf/tarski
    cd tarski
    pip install -e .

This will install the project in "editable mode", i.e., by using the actual files from the project directory
tree, as opposed to a copy installed in some system or virtualenv directory. Any modification to the files
will thus be immediately reflected in the _installed_ library.


## Testing 
All of Tarski's tests live under the `tests` directory (shocking!).
To run them, you just need to run `pytest` (`pip install pytest`) on the root directory.
You can also run `tox` (`pip install tox`) to have some additional checks (e.g., style checks) run.



## Software Requirements
Tarski requires Python >= 3.5.
The above installation instructions will install under the hood a number of dependencies, among which
numpy and scipy.


### Supported Languages
At the moment, Tarski is able to parse the following modeling languages:
* PDDL
* Functional STRIPS

with the following limitations:
* The PDDL `either` keyword for defining compound types is not supported. 
* Parsing of derived predicates is not supported yet.

## Modules

* Description Logic (`tarski.dl`)
* PDDL / FSTRIPS parsing and writing (`tarski.io`)
