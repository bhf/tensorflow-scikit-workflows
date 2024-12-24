# Tensorflow-Scikit Workflows 

Demonstration of a project structure for common machine learning workflows. Uses Tensorflow and Scikit with a monorepo structure. 

An example of executing via REST (FastAPI) is also included.

## Setup and Install

### Create a Virtual Environment

```bash
$ pyenv virtualenv 3.11.9 tf-sk-workflows
```

### Activate Existing Virtual Environment

```bash
$ pyenv local tf-sk-workflows
```

## Install

```bash
poetry install
``` 

## Project Structure

`core`
Core classes and abstractions related to all models, representations of model performance and comparison utils.

`sklearnworkflows`
Machine learning pipelines implemented using Sklearn.

`tensorflowworkflows`
Machine learning pipelines implemented using Tensorflow.

`api` A simple FastAPI interface that exposes some API endpoints to demonstrate executing the workflows via REST.

## API and Swagger Spec

### Run API Server

```bash
poetry run python api
```

### Swagger Spec

Available at: 

SwaggerUI: http://localhost:3001/docs

Redoc: http://localhost:3001/redoc

JSON Spec: http://localhost:3001/openapi.json
