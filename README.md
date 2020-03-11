
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
along with modules to perform other common tasks such as logical transformations,
reachability analysis, grounding of first-order representations and problem reformulations.


**Installation**: Check the [*installation instructions*](docs/installation.md).

**Documentation**: Read the [*documentation of the project*](https://tarski.readthedocs.io).

**Testing**: Most tests can be run by executing `pytest` on the root directory.
Alternatively, they can be run through `tox`, for which several testing environments [are defined](tox.ini).

## License
Tarski is licensed under the [GNU General Public License, version 3](LICENSE).
