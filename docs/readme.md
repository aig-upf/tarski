
# Tarski - Documentation

We currently use a mixture of reStructuredText, markdown and Jupyter notebooks for our documentation.
Everything under this `docs` directory is automatically built on the <https://readthedocs.org/> servers
on every push to the main branches of the repo. The main docs are served under
<https://tarski.readthedocs.io/en/latest/>, while the docs for the devel branch, for instance, are served
under <https://tarski.readthedocs.io/en/devel/>.

Readthedocs thus parses the whole `docs` directory and generated the documentation through the
[Sphinx](https://www.sphinx-doc.org/en/master/) generator. If you need to fine-tune some readthedocs options
through their web interface, you'll need to create a user at <https://readthedocs.org/> and ask Guillem
to add you to the list of people with "maintainer" rights.
 
In any case, the file `conf.py` contains our specific Sphinx setup, which includes, among others,
instructions to load plugins that enable the parsing and rendering of markdown and even the execution
of Jupyter notebooks.


## Building the docs locally

You should be able to generate the docs locally by a similar procedure than the one used by readthedocs.
For this, you need to install the `docs` Tarski specified in `setup.py`, e.g. by running: 

    pip install -e .[docs]

And then you should be able to bootstrap Sphinx by running from the `docs` directory:

    make html
    
The generated docs are left in `_build/html/index.html`
    
    
## Some useful links

* `.readthedocs.yml` [configuration file](https://docs.readthedocs.io/en/stable/config-file/v2.html). 