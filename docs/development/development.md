
# Development Notes

## Code Style

We aim at following the [PEP 8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/).
Many Python IDEs support on-the-fly PEP 8 style checks; we additionally use
[pylint](https://pylint.readthedocs.io/en/latest/) and
[pycodestyle](https://pycodestyle.readthedocs.io/en/latest/).
You can check code compliance by running e.g. `tox -e pylint`.

## Project Structure
We follow a [`src`-based](https://blog.ionelmc.ro/2014/05/25/python-packaging/) project structure.

## Installation
Tarski aims at being a full-fledged Python package that can be installed with a simple `pip install tarski`.

## Testing
Tests are written using `pytest` and can be run by issuing `pytest` on the project root directory,
provided that the `pytest` module has been installed.

You can also run the tests from a virtual environment where the whole setup process that a new user would follow is 
entirely replicated by using [`tox`](http://tox.readthedocs.io/).
