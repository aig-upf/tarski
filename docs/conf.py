# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sys
import os
import importlib


from recommonmark.transform import AutoStructify
sys.path.insert(0, os.path.abspath(os.path.join('..', 'src')))

# Load the version number from ../src/tarski/version.py
root = os.path.abspath(os.path.join('..'))
spec = importlib.util.spec_from_file_location('tsk.version', os.path.join(root, 'src/tarski/version.py'))
tskversion = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tskversion)


# -- Project information -----------------------------------------------------

project = 'Tarski'
copyright = '2019-2020, Miquel Ramírez and Guillem Francès'
author = 'Miquel Ramírez and Guillem Francès'

# The short X.Y version.
version = tskversion.__version__
# The full version, including alpha/beta/rc tagss
release = tskversion.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'nbsphinx',  # To use Jupyter notebooks within the documentation <https://nbsphinx.readthedocs.io/en/0.4.2/>
    'sphinx.ext.mathjax',  # To render latex in the generated HTML
    'recommonmark',  # To use markdown documents as well
]

# This forces the jupyter notebooks to be executed every time the docs are built by sphinx
nbsphinx_execute = 'always'


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'requirements.txt']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Default language for syntax highlighting in reST and Markdown cells
highlight_language = 'python3'

# see http://www.sphinx-doc.org/en/master/usage/markdown.html for instructions on markdown integration
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'Recommonmarkdoc'

# TODO: Remove this once we discover how to install or mock Gringo in the
#       Readthedocs servers.
if os.environ.get('READTHEDOCS') == 'True':
    nbsphinx_allow_errors = True


# app setup hook
def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
    }, True)
    app.add_transform(AutoStructify)
