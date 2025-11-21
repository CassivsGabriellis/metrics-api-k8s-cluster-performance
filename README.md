# Metrics API – Kubernetes Deployment & CI/CD (FastAPI | k3s | Terraform | Ansible | GitHub Actions)

**[Article explaning this project](https://www.foliocassianico.com.br/en/posts/api-k8s-server/)**

This repository contains the **CI/CD pipeline** responsible for building, publishing, and deploying the Metrics API into a **k3s Kubernetes cluster running on an AWS EC2 instance**.

The main application code, Kubernetes manifests, and infrastructure are stored in separate directories. This repository focuses specifically on the **automation workflow** that enables continuous delivery of the API.

## What This Repository Does

* **Builds the Docker image** for the Metrics API using GitHub Actions.
* **Pushes the image** to Docker Hub with both `latest` and commit-SHA tags.
* **Connects via SSH** to the EC2 instance hosting the k3s cluster.
* **Updates the Deployment** by applying the new container image through:

  ```sh
  kubectl set image deployment/metrics-api-deployment
  ```
* **Waits for rollout** to ensure the new version becomes healthy.

This pipeline allows any code change pushed to `main` to be **automatically deployed** to the running cluster, with no manual steps required.

## Requirements

The following GitHub Secrets must be configured:

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_TOKEN`
* `EC2_HOST` (Elastic IP assigned by Terraform)
* `EC2_SSH_USER` (e.g., `ubuntu`)
* `EC2_SSH_KEY` (private SSH key contents)

## Purpose

This repository exists purely to manage the **automated delivery pipeline**, keeping CI/CD logic cleanly separated from the application code and infrastructure provisioning. It demonstrates a complete Cloud/DevOps workflow using:

* FastAPI
* Docker
* Kubernetes (k3s)
* Terraform
* Ansible
* GitHub Actions