## About

How to test [latex-git-hooks]

## Local

* Create git repo `latex-git-hooks-test-repo-local```
	```
	cd ..
	mkdir latex-git-hooks-test-repo-local
	cd latex-git-hooks-test-repo-local
	git init
	```
* Copy `Taskfile_local.yml` as `Taskfile.yml`
* Copy `*.tex` files from `tests/data`
* Add `*.tex` to git index
* Initiate and activate virtualenv
* Run all git hooks
	```
	task hook-all
	```

## Remote

* Create git repo `latex-git-hooks-test-repo-remote```
	```
	cd ..
	mkdir latex-git-hooks-test-repo-remote
	cd latex-git-hooks-test-repo-remote
	git init
	```
* Copy `Taskfile_remote.yml` as `Taskfile.yml`
* Create `.pre-commit-config.yaml` with hooks to be tested
* Copy `*.tex` files from `tests/data`
* Add `*.tex` to git index
* Initiate and activate virtualenv
* Install git hooks
	````
	task pre-commit-install
	```
* Run git hooks
	````
	task pre-commit-run
	```