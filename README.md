# 🐍 Flask Market App – CI/CD with Docker, GitHub Actions, and Kubernetes

This project is a sample Flask web app demonstrating how to:
- Dockerize a Python application
- Automate builds & pushes with GitHub Actions
- Deploy to Kubernetes using Minikube

---

## 🔧 Tech Stack

- Python 3.11
- Flask
- Docker
- GitHub Actions (CI/CD)
- Kubernetes + Minikube

---

## 🚀 Getting Started

### 1. Clone the repo

```
git clone https://github.com/your-username/flask-market-app.git
cd flask-market-app

### 2. Run locally
pip install -r requirements.txt
python app.py

Visit: http://localhost:5000

### 🔐 Secrets & Security
Docker credentials are stored in GitHub Secrets
    1. DOCKER_USERNAME
    2. DOCKER_PASSWORD

### 3. Docker build and run locally
docker build -t market-flaskapp .
docker run -d -p 5000:5000 market-flaskapp
(These are used in the GitHub Actions workflow for Docker Hub login and image push.)

Visit: http://localhost:5000

### 4. 🤖 GitHub Actions CI/CD
Workflow file: .github/workflows/ci.yml

### 5. ☸️ Kubernetes (Minikube)
minikube start

### Apply Kubernetes Manifest
kubectl apply -f k8s/flask-deployment.yaml
kubectl apply -f k8s/flask-service.yaml

### Access the App
Expose the app via NodePort:
minikube service flask-service

This will open your browser at a URL like http://localhost:30000

### You can see app background in screenshot folder.