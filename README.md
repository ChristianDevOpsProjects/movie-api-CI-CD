🎬 Movie API – Docker + Kubernetes + CI/CD

A simple FastAPI-based movie API designed to demonstrate containerization, Kubernetes deployment, auto-scaling, and CI/CD with GitHub Actions.
This project is beginner-friendly, but still shows production-ready practices.

🗂 Project Structure
movie-api/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
└── README.md

⚡ Features

FastAPI API serving a list of movies

Dockerized for easy deployment

Kubernetes Deployment with multiple pods

Horizontal Pod Autoscaler for auto-scaling

CI/CD Pipeline with GitHub Actions

🏗 Tech Stack

API: Python, FastAPI

Containerization: Docker

Orchestration: Kubernetes

CI/CD: GitHub Actions

Optional: Run Kubernetes locally with k3d
 or kind
.

🚀 Getting Started
1. Run Locally with Docker
# Build the Docker image
docker build -t movie-api:latest ./app

# Run the container
docker run -p 8000:8000 movie-api:latest


Visit http://localhost:8000/movies
 to see the API in action.

2. Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml


Starts 2 pods by default

Auto-scales up to 5 pods if CPU usage exceeds 50%

3. CI/CD with GitHub Actions

Push changes to the main branch:

GitHub Actions builds and tests the API

Docker image is built and pushed to GitHub Container Registry

Kubernetes deployment is updated automatically

This makes your API production-ready with minimal effort.

🎯 Why This Project Stands Out

Shows modern DevOps skills in a simple project

Demonstrates scaling and deployment best practices

Beginner-friendly yet practical and impressive for recruiters


📌 References

FastAPI Docs

Docker Docs

Kubernetes Docs

GitHub Actions Docs
