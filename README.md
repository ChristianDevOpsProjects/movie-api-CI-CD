# 🎬 Movie API – Docker + Kubernetes + CI/CD

A **scalable, production-ready API** built with FastAPI, Docker, and Kubernetes, featuring GitHub Actions CI/CD.  
This project demonstrates **containerization, deployment, auto-scaling, and pipeline automation** — perfect for showcasing cloud-native skills to recruiters.

---

## 🚀 Features

- **FastAPI API** serving movie data
- **Dockerized** for easy container deployment
- **Kubernetes Deployment** with multiple pods
- **Horizontal Pod Autoscaler** for scaling based on CPU
- **CI/CD Pipeline** using GitHub Actions
- Beginner-friendly, fully functional pipeline

---

## 🏗 Tech Stack

- **API:** Python, FastAPI
- **Containerization:** Docker
- **Orchestration:** Kubernetes
- **CI/CD:** GitHub Actions
- **Optional Local Kubernetes:** [k3d](https://k3d.io/) or [kind](https://kind.sigs.k8s.io/)

---

## 🗂 Project Structure
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

yaml
Copy code

---

## ⚡ Quick Start

### 1. Run Locally with Docker

```bash
docker build -t movie-api:latest ./app
docker run -p 8000:8000 movie-api:latest
Visit http://localhost:8000/movies to see the API.

2. Deploy to Kubernetes
bash
Copy code
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
Deployment runs 2 pods by default

Horizontal Pod Autoscaler will scale pods automatically under load

3. CI/CD with GitHub Actions
Push any changes to main branch → GitHub Actions will:

Build and test the app

Build and push the Docker image to GitHub Container Registry

Deploy the latest version to your Kubernetes cluster
