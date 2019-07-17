
# Tarski - An AI Planning Modeling Framework 
[![Build Status](https://travis-ci.com/aig-upf/tarski.svg?branch=master)](https://travis-ci.com/aig-upf/tarski)
[![codecov](https://codecov.io/gh/aig-upf/tarski/branch/master/graph/badge.svg)](https://codecov.io/gh/aig-upf/tarski)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tarski.svg?style=popout)
![PyPI](https://img.shields.io/pypi/v/tarski.svg?style=popout)


## What is Tarski
Tarski is a framework for the specification, modeling and manipulation of 
[AI planning](https://en.wikipedia.org/wiki/Automated_planning_and_scheduling) problems.
Tarski is written in Python and includes parsers for major modeling languages
(e.g., [PDDL](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language),
[FSTRIPS](https://dl.acm.org/citation.cfm?id=566359),
[RDDL](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language#RDDL)), 
along with modules to perform common tasks such as reachability analysis and grounding of first-order representations.


## Installation

You can install the latest Tarski release with

    pip install tarski

If instead you want to use the latest code available on the Github repository, use 
    
    pip install -U git+https://github.com/aig-upf/tarski.git


## Development
If developing Tarski, we recommend cloning from the Github repository and doing a dev installation
(the`-e` flag for `pip`) on a [virtual environment](https://docs.python.org/3/tutorial/venv.html):
    
    git clone https://github.com/aig-upf/tarski
    cd tarski
    pip install -e .

This will install the project in "editable mode", meaning that any modification to the files
is immediately reflected in the _installed_ library.


## Testing 
All of Tarski's tests live under the `tests` directory (shocking!).
To run them, you just need to run `pytest` (`pip install pytest`) on the root directory.
You can also run `tox` (`pip install tox`) to have some additional checks (e.g., style checks) run.



## Software Requirements
Tarski requires Python >= 3.5.
The above installation instructions will install transparently for you a number of additional dependencies, among which
`numpy`, `scipy` and `pyrddl`.


## Known Limitations
At the moment, Tarski is able to parse problems specified in PDDL, Functional STRIPS and RDDL, 
but (1) parsing of derived predicates is not supported yet, and (2)
the PDDL `either` keyword for defining compound types is not supported, and it is unlikely it will ever be. 
