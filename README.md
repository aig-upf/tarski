
# Tarski - An AI Planning Modeling Framework 
[![Build Status](https://travis-ci.com/aig-upf/tarski.svg?branch=master)](https://travis-ci.com/aig-upf/tarski)
[![Documentation Status](https://readthedocs.org/projects/tarski/badge/?version=latest)](https://tarski.readthedocs.io/en/latest/?badge=latest)
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
along with modules to perform other common tasks such as reachability analysis and 
grounding of first-order representations.


Read the (work-in-progress) documentation of the project in <https://tarski.readthedocs.io>.


## Installation

Install the latest Tarski release with

    pip install tarski

If instead you want to use the latest code available on the Github repository, use 
    
    pip install -U git+https://github.com/aig-upf/tarski.git

## Extras

Tarski allows the _optional_ installation of an `sdd` module that allows to interact
with the [PySDD package](https://github.com/wannesm/PySDD) for sentential decision diagrams.
To use this `tarski.sdd` optional package, you'll need to pip install with the `sdd` extra, as in: 

    pip install tarski[sdd]

Support for this is still experimental, as the installation of PySDD does not seem to be
too pip-friendly.

### Software Requirements
Tarski requires Python >= 3.6. The above installation instructions will install transparently 
for you a number of additional dependencies, among which `numpy`, `scipy` and `pyrddl`.


## Development and Testing
If developing Tarski, we recommend cloning from the Github repository and doing a dev installation
(the`-e` flag for `pip`) on a [virtual environment](https://docs.python.org/3/tutorial/venv.html):
    
    git clone https://github.com/aig-upf/tarski
    cd tarski
    pip install -e .

This will install the project in "editable mode", meaning that any modification to the files
is immediately reflected in the _installed_ library.


**Testing**. All of Tarski's tests live under the `tests` directory.
To run them, you just need to run `pytest` (`pip install pytest`) on the root directory.
You can also run the tests through `tox` (`pip install tox`), for which several testing environments
[have been defined](tox.ini), e.g. to test the framework under different Python versions or apply static
analysis to the code.


## Known Limitations
At the moment, Tarski is able to parse problems specified in PDDL, Functional STRIPS and RDDL, 
but (1) parsing of derived predicates is not supported yet, and (2)
the PDDL `either` keyword for defining compound types is not supported, and it is unlikely it will ever be.
Additionally, and for compatibility reasons with old standard benchmarks, the parser represents all predicate,
function (including constants) and PDDL types (i.e. FOL sorts) _in lowercase_.  

## License
Tarski is licensed under the [GNU General Public License, version 3](LICENSE).
