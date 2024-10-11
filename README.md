## About

This is a personal [git hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) collection for LaTeX documents using [pre-commit](https://github.com/pre-commit/pre-commit). It helps you to increase quality of LaTeX document. 

For more advanced [pre-commit](https://github.com/pre-commit/pre-commit) hooks for LaTeX documents check the project [jonasbb/pre-commit-latex-hooks](https://github.com/jonasbb/pre-commit-latex-hooks). A number of git hook in this repo are using some ideas from the mentioned project (primary the one using `pygrep` and `regex`).

### Installation

1. Install pre-commit:
    ```
    pip install --upgrade pre-commit
    ```
1. Add the hook to your `.pre-commit-config.yaml` file:
    ```yaml
    repos:
    - repo: https://github.com/vdmitriyev/latex-git-hooks
      rev: v0.2.0
      hooks:
      - id: validate-filename
      - id: check-latex-packages
      - id: ignore-auxiliary-files
      - id: no-space-in-cite
      - id: no-space-in-citep
      - id: comma-in-eg-ie
      - id: check-single-command-per-line
      - id: run-linter-paperlinter
        
    - repo: https://github.com/pre-commit/pre-commit-hooks
      rev: v3.3.0
      hooks:
      - id: check-merge-conflict
      - id: check-yaml
    ```
1. Run to install dependencies:
    ```
    pre-commit install 
    ```
1. Run `pre-commit` explicitly:
    ```
    pre-commit run --all-files
    ```
1. Run `pre-commit` in verbose mode:
    ```
    pre-commit run --all-files --verbose
    ```

## Usage

The hook will automatically run before every commit. It will check your LaTeX files and report any issues. You will need to fix the issues before committing your changes.

## Notes on `hooks`

* `run-linter-paperlinter`
	- linter hook will always exists successful and shows what has been found by linter

## LaTeX Linters

Besides git hooks, `linters` for `LaTeX` could be used to improve quality. Please, consider following `linters`:

* `chktexrc`
    - ChkTeX - LaTeX semantic checker - https://www.nongnu.org/chktex/
* `latexcheck-py`
    - https://github.com/dainiak/latexcheck-py
* `Paper-Linter`
    - https://github.com/misc0110/Paper-Linter

### Development: tests

* Check `tests` directory to test using `pytests`
* Check `tests/taskfiles` directory to test using local and remote git repositories

### Development: taskfile

* Prerequisite: [taskfile](https://taskfile.dev/installation/) must be installed
* Package: list avaialbe tasks:
	```
	task 
	```

## Configuration

Currently, extra no configuration other then options in [`.pre-commit-config.yaml`](#installation) are available

## Contributing

Contributions are welcome! Feel free to submit pull requests with new features, bug fixes or tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.