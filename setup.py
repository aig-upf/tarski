from setuptools import setup, find_packages
from codecs import open
import importlib
import os

root = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Load the version number from ./src/tarski/version.py
spec = importlib.util.spec_from_file_location('tsk.version', os.path.join(root, 'src/tarski/version.py'))
version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version)


def main():

    setup(
        name='tarski',
        version=version.__version__,
        description='Tarski is a framework for the specification, modeling and manipulation of AI planning problems.',
        long_description=long_description,
        long_description_content_type='text/markdown',

        url='https://github.com/aig-upf/tarski',
        author='Miquel Ramírez and Guillem Francès',
        author_email='guillem.frances@upf.edu',

        keywords='planning logic STRIPS RDDL',
        classifiers=[
            'Development Status :: 3 - Alpha',

            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',

            'Topic :: Scientific/Engineering :: Artificial Intelligence',

            "License :: OSI Approved :: Apache Software License",

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],

        packages=find_packages('src'),  # include all packages under src
        package_dir={'': 'src'},  # tell distutils packages are under src

        python_requires='>=3.6',  # supported Python ranges
        install_requires=[
            # psutil not supported on Windows, we haven't tested in other platforms, but since it's not essential
            # to the functioning of Tarski, better be conservative here and install only on Linux.
            'psutil; platform_system=="Linux"',

            'multipledispatch',

            # Antlr pinned to a specific version to avoid messages "ANTLR runtime and generated code versions disagree"
            # messages. If we want to bump this up, we'll need to regenerate the grammar files with the new version.
            'antlr4-python3-runtime==4.7.2',
        ],

        extras_require={
            'test': [
                'pytest',
                'tox',
                'pytest-cov',
                'mypy'
            ],
            'docs': [
                # We pin the Jinja2 version here as there seems to be some incompatibility between later Jinja3 releases
                # and nbsphinx. Hopefully we can bump this up in the future.
                'jinja2==2.11.3',
                # We also pin the docutils version due to incompatibilities with nbsphinx,
                # see https://github.com/sphinx-doc/sphinx/issues/9001
                'docutils<0.17',
                'sphinx==3.5.4',
                'nbsphinx==0.8.5',
                'recommonmark==0.7.1',
                'sphinx_rtd_theme==0.5.2',
                'ipykernel==5.5.5',
                'ipython==7.24.0'
            ],
            'arithmetic': [
                'scipy',
                'numpy'
            ],
            'rddl': [
                "pyrddl @ https://github.com/thiagopbueno/pyrddl/archive/9ccab6a.zip#sha1=a584f90381bf7d48b85976807b9bc6c0cb2761ba"
            ],
        },

        # This will include non-code files specified in the manifest, see e.g.
        # http://python-packaging.readthedocs.io/en/latest/non-code-files.html
        include_package_data=True,
    )


if __name__ == '__main__':
    main()
