
# Installation

## Software Requirements
Tarski only requires `Python >= 3.6`. The installation instructions below will install 
for you any additional required dependencies, among which `numpy`, `scipy` and `pyrddl`.


## Installing Tarski

Install the latest Tarski release with

    pip install tarski

If instead you want to use the latest code available on the Github repository, use 
    
    pip install -U git+https://github.com/aig-upf/tarski.git
    

## Installing Tarski in development mode
If developing Tarski, we recommend cloning from the Github repository and doing a dev installation
(the`-e` flag for `pip`) on a [virtual environment](https://docs.python.org/3/tutorial/venv.html):
    
    git clone https://github.com/aig-upf/tarski
    cd tarski
    pip install -e .

This will install the project in "editable mode", meaning that any modification to the files
is immediately reflected in the _installed_ library.
