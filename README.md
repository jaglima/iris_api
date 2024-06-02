# Iris Dataset Classifier API

This is a FastAPI-based API that classifies Iris flower species based on sepal and petal dimensions.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Create Conda Environment](#create-conda-environment)
  - [Run Locally](#run-locally)
  - [Run with Docker](#run-with-docker)
- [Usage](#usage)
  - [Example Requests](#example-requests)
- [Acknowledgments](#acknowledgments)

## Overview

This API takes measurements of sepal length, sepal width, petal length, and petal width, and predicts the species of the Iris flower.

## Features

- Predict the species of Iris flower using a pre-trained machine learning model.
- Easy to use with JSON payloads.
- Lightweight and fast with FastAPI.

## Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/iris-classifier-api.git
cd iris-classifier-api
```

### Create Conda Environment
```bash
conda create -n iris-api python=3.9
conda activate iris-api
pip install -r requirements.txt
```
### Run

#### Locally:
```bash
uvicorn src.app:app --reload
```
#### Docker
```bash
docker run -d -p 8000:8000 iris-classifier-api
```

### Usage
You can interact with the API using curl commands. The API listens on port 8000 by default.

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"sepal_length": 6.2, "sepal_width": 3.4, "petal_length": 5.4, "petal_width": 2.3}'
```

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"sepal_length": 4.7, "sepal_width": 3.2, "petal_length": 1.3, "petal_width": 0.2}'
```
