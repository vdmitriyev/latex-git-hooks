## About

This is a personal [git hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) collection for LaTeX documents using [pre-commit](https://github.com/pre-commit/pre-commit). It helps you to increase quality of LaTeX document. 

For more advanced [pre-commit](https://github.com/pre-commit/pre-commit) hooks for LaTeX documents check the project [jonasbb/pre-commit-latex-hooks](https://github.com/jonasbb/pre-commit-latex-hooks).

### Installation

1. Install pre-commit: 
    ```
    pip install --upgrade pre-commit
    ```
1. Add the hook to your `.pre-commit-config.yaml` file
    ```yaml
    repos:
    - repo: https://github.com/vdmitriyev/latex-git-hooks
      rev: v0.1.0
      hooks:
      - id: validate-filename
	  - id: check-latex-packages
        
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
1. Run `pre-commit` explicitly
	```
	pre-commit run --all-files
	```
1. Run `pre-commit` in verbose mode
	```
	pre-commit run --all-files --verbose
	```

## Usage

The hook will automatically run before every commit. It will check your LaTeX files and report any issues. You will need to fix the issues before committing your changes.

## Configuration

Currently, no configuration options are available.  Future features may offer customization.

## Contributing

We welcome contributions! Feel free to submit pull requests with new features or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.