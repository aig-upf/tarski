
# Development Notes

## Requirements and Dependencies

Development of Tarski currently happens under Python 3.

## Code Style

We aim at following the [PEP 8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/).
Many Python IDEs support on-the-fly PEP 8 style checks, and there are also external tools
to help the code comply with the style guidelines, such as [Google's YAPF](https://github.com/google/yapf).
We might consider using one of these down the road.


## Testing
Tests are written using `pytest` and can be run by issuing `pytest` on the project root directory,
provided that the `pytest` module has been installed.


### Running the test from a virtual environment
We can run the tests from a virtual environment where the necessary dependencies have been
installed first:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install pytest scipy
```

Once this has been done, running `pytest` will work the same, but we avoid the need for
doing a system-wide installation of all the project dependencies.
We are currently testing whether [tox](https://tox.readthedocs.io/en/latest/) 
might be a good option for the project in order to automatize running tests on different supported 
Python versions.