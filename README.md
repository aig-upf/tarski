
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


**Documentation**: Read the (work-in-progress) *documentation* of the project at
<https://tarski.readthedocs.io>.

**Installation**: Check the [*installation instructions*](docs/installation.md).

**Testing**. All of Tarski's tests live under the `tests` directory.
To run them, you just need to run `pytest` (`pip install pytest`) on the root directory.
You can also run the tests through `tox` (`pip install tox`), for which several testing environments
[have been defined](tox.ini).


## Known Limitations
At the moment, Tarski is able to parse problems specified in PDDL, Functional STRIPS and RDDL, 
but (1) parsing of derived predicates is not supported yet, and (2)
the PDDL `either` keyword for defining compound types is not supported, and it is unlikely it will ever be.
Additionally, and for compatibility reasons with old standard benchmarks, the parser represents all predicate,
function (including constants) and PDDL types (i.e. FOL sorts) _in lowercase_.  

## License
Tarski is licensed under the [GNU General Public License, version 3](LICENSE).
