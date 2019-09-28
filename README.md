# Objective
testing python3 in docker

# What I leaned
```console
venv inside the project is only for u to run it via native host including the IDE
if u want to install it via the pipenv, u need to run `pipenv install sanic` then it will update the `Pipfile` and `Pipfile.lock`
As pipenv will also create a venv for u in a cache place which u can check it via `pipenv --venv`
```

# tools
```
python
version management: pyenv
package management: pipenv
test framework: pytest
web framework: sanic
Docker native: python
Dokcer pypy: pypy:3
```


# Docker build
```console
docker build . -t hello-py
```

# venv
```console
python -m venv ./venv
```

# Reference
1. https://pythonspeed.com/articles/pipenv-docker/
