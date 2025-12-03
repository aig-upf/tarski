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
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            "License :: OSI Approved :: Apache Software License",
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
            'Programming Language :: Python :: 3.14',
        ],

        packages=find_packages('src'),  # include all packages under src
        package_dir={'': 'src'},  # tell distutils packages are under src

        python_requires='>=3.10',
        install_requires=[
            # psutil not supported on Windows, we haven't tested in other platforms, but since it's not essential
            # to the functioning of Tarski, better be conservative here and install only on Linux.
            'psutil; platform_system=="Linux"',

            'multipledispatch',

            # Pin down ANTLR to the same version with which the python runtime grammars were generated.
            # This prevents "ANTLR runtime and generated code versions disagree" messages and the potential bugs
            # caused by version mismatches.
            # If you want to change this version, regenerate the grammars as described in
            # src/tarski/io/_fstrips/readme.md
            'antlr4-python3-runtime==4.13.2',
        ],

        extras_require={
            'test': [
                'pytest>=7.0.1',
                'tox',
                'pytest-cov',
                'mypy',
                "pre-commit~=4.5.0",
                "ruff~=0.14.7",
            ],
            'docs': [
                'jinja2==3.1.6',
                'docutils',  # Let sphinx figure the version out
                'sphinx==8.2.3',
                'nbsphinx==0.9.8',
                'recommonmark==0.7.1',
                'sphinx_rtd_theme==3.0.2',
                'ipykernel==7.1.0',
                'ipython==9.8.0'
            ],
            'arithmetic': [
                'scipy',
                'numpy'
            ],
            'rddl': [
                "pyrddl"
            ],
            'parsegen': [
                'ply==3.11'
            ],
            'clingo': [
                # Clingo (& gringo) bindings to the clingo solver
                'clingo>=5.5.1'
            ],
            'stubs': [
                'types-psutil',
            ]
        },

        # This will include non-code files specified in the manifest, see e.g.
        # http://python-packaging.readthedocs.io/en/latest/non-code-files.html
        include_package_data=True,
    )


if __name__ == '__main__':
    main()
