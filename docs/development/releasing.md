
# Creating Tarski releases

The release process and upload of packages to `pypi` is semi-automated, and involves creating a pull
request from `devel` to `master`, then merging it and creating a GH release (that will automatically
trigger the `pypi` upload).
The list of detailed steps is as follows:

1. Make sure you're in the `devel` branch.
2. Update the version number in `src/tarski/version.py`
3. Update the `CHANGELOG.md` file manually to reflect the changes since the last release.
4. Don't forget to commit & push the changes.
5. Create a PR against the `master` branch.
6. Once all workflows have executed successfully, merge the PR.
7. Create a [new release](https://github.com/aig-upf/tarski/releases/new) in the GH repo,
   with an appropriate tag such as `v0.6.0`. The new release will trigger a GH workflow that will
   automatically upload the package to `pypi`.

## Relevant Pointers
* <https://packaging.python.org/tutorials/packaging-projects/>
* <https://github.com/pypa/gh-action-pypi-publish>
* <https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#publishing-to-package-registries>
* <https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>
