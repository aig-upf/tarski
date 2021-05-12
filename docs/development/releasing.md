
# Release Process

## Uploading a Tarski release to the Python Package Index

Docs: <https://packaging.python.org/tutorials/packaging-projects/>

1. Update the `CHANGELOG.md` file.
1. Update the version number in `src/tarski/version.py`
1. Commit. Use message like "Preparing for release 0.6.0".
1. Go to the `master` branch and merge the `devel` branch.
1. Tag the release.
    ```bash
        export TARSKI_RELEASE="v0.2.0"
        git tag -a ${TARSKI_RELEASE} -m "Tarski release ${TARSKI_RELEASE}"
    ```
        
1. Run the following instructions from the root directory of the project:
    ```bash
        python3 -m pip install --upgrade twine setuptools wheel  # (optional)
    
        rm -rf dist/
        python3 setup.py sdist bdist_wheel
    
        # Test first (result will go to https://test.pypi.org/project/tarski/):
        python3 -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
    
        # Then go!
        python3 -m twine upload --skip-existing dist/*
    ```

1. Push all code changes plus the tag to the repo:
    ```bash
        git push && git push origin ${TARSKI_RELEASE}
    ```

1. Check the [Github releases page](https://github.com/aig-upf/tarski/releases) to make sure the new release appears
   there and can be downwloaded.

