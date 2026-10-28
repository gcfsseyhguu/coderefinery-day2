# CodeRefinery Day 2 starter

A small Python teaching project for the NLTU workshop with Yuriy Paslavskyi. It
introduces simple functions, tests, Git branches, pull requests, GitHub Actions,
and AI-assisted project documentation.

## Project files

- `example.py` contains `add` and `subtract`, along with tests for both
  functions.
- `requirements-dev.txt` lists the development dependency, pytest.
- `.github/workflows/ci.yml` defines the GitHub Actions workflow that runs the
  tests.
- `LICENSE` contains the project's MIT license.
- `README.md` documents the project and how to use it.

## Set up on Windows with Git Bash

Install Git for Windows and Python 3.13, then open Git Bash in the project
folder. Python 3.13 is the version used by CI. Create and activate a virtual
environment, then install the development dependencies:

```bash
py -3.13 -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements-dev.txt
```

To leave the virtual environment when you are done, run `deactivate`.

## Try the functions and run tests

Try the functions from Git Bash:

```bash
python -c "from example import add, subtract; print(add(3, 4)); print(subtract(4, 3))"
```

Run all tests currently in the project:

```bash
python -m pytest -v example.py
```

The tests are defined in `example.py`. This repository does not currently
contain `recipes.py` or a `tests/` directory.

## Continuous integration

The GitHub Actions workflow installs Python 3.13 and the dependencies in
`requirements-dev.txt`, then runs `python -m pytest -v example.py` on
`ubuntu-latest`. It has a five-minute timeout and read-only contents
permissions.

The workflow runs when a commit is pushed to `main`, when a pull request
targeting `main` is opened or updated, or when someone starts it manually with
`workflow_dispatch`. A push to a feature branch without a pull request does not
trigger it under the current branch filter.

To view a run, open the repository on GitHub, select **Actions**, choose the
**Python tests** workflow, and open a run. Select the **tests** job to see the
steps and their logs, including the pytest output.

## Start your own project

1. Select **Use this template → Create a new repository** on GitHub.
2. Create the repository in your own account; include only the default branch.
3. Clone **your new repository** and open its folder in VS Code.

## License and sources

This teaching adaptation is distributed under the [MIT License](LICENSE). See
that file for the license terms and copyright notice.

The project follows the learning pattern of [CodeRefinery testing](https://coderefinery.github.io/testing/)
and [full-cycle collaboration](https://coderefinery.github.io/testing/full-cycle-ci/).
Prepared with AI assistance; the local test checkpoints were checked
separately.
