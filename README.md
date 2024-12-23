# Tensorflow-Scikit Workflows 

## Setup and Install

### Create a Virtual Environment

```bash
$ pyenv virtualenv 3.11.9 tf-sk-workflows
```

### Activate Existing Virtual Environment

```bash
$ pyenv local tf-sk-workflow
```

## Install

```bash
poetry install
``` 

## Run Unit Tests

cd into each module before running:

```bash
poetry run pytest
```

## API and Swagger Spec

### Run API Server

```bash
poetry run python api
```

### Swagger Spec

Available at: 

Web frontend: http://localhost:3001/docs

JSON Spec: http://localhost:3001/openapi.json

## Project Structure

`core`
Core classes related to all models, representations of model performance and comparison utils.

`sklearnworkflows`
Machine learning pipelines implemented using Sklearn.
This package depends on `core`

`tensorflowworkflows`
Machine learning pipelines implemented using Tensorflow.
This package depends on `core`

`api` A simple FastAPI interface