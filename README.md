🎬 Movie API – Docker + Kubernetes + CI/CD

A simple FastAPI-based movie API designed to show how to build and deploy a scalable service using Docker, Kubernetes, and GitHub Actions CI/CD.

It’s beginner-friendly but still demonstrates production-ready skills like containerization, auto-scaling, and automated deployment.

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

You can also run this locally on Kubernetes using k3d
 or kind
.

🚀 Getting Started
Run Locally with Docker
# Build the Docker image
docker build -t movie-api:latest ./app

# Run the container
docker run -p 8000:8000 movie-api:latest


Open http://localhost:8000/movies
 in your browser to see the API in action.

Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml


Starts with 2 pods by default

Auto-scales up to 5 pods if CPU usage goes above 50%

This shows how your app can handle more load automatically, just like in a real production environment.

CI/CD with GitHub Actions

Push changes to the main branch, and GitHub Actions will:

Build and test your API

Build and push a Docker image to GitHub Container Registry

Deploy the updated app to your Kubernetes cluster

This setup demonstrates modern DevOps practices in a simple, easy-to-understand way.
