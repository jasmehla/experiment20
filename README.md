# Experiment 20: CI/CD Pipeline with Docker Compose

## Objective

Implement a CI/CD pipeline using Docker and GitHub Actions for backend testing with MySQL integration.

## Tech Stack

* Python (Flask)
* MySQL
* Docker & Docker Compose
* GitHub Actions

## Steps to Run

1. Build and run containers:
   docker compose up --build

2. Stop containers:
   docker compose down

## CI/CD

On every push or pull request:

* Docker containers are built
* Backend tests are executed using pytest

## Output

* Backend connects to MySQL successfully
* Tests pass via Docker and CI/CD pipeline
