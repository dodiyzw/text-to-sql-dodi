# text-to-sql using LLM

## Summary

## Getting Started



There are multiple ways to spin up this project, listed below.

### Option 1: Spin up using Python
- To begin, first install the required python packages by running

  ```pip install -r requirements.txt```
- To spin up using python, navigate to `main/frontend` and run:
  `streamlit run streamlit-sql.py`


### Option 2: Spin up using Docker compose (**note that this requires you to also have Docker installed)**:
-   `docker-compose up`

- Navigate to `localhost:8501` to interact with the app. 

### Option 3: Spin up using Kubernetes cluster:

  - Navigate to `main/deployment`. 
  - Run `sh setup_cluster.sh`.
  - Navigate to `localhost:8501` once port-forwarding has started. 

  **Note: This approach is not perfected and currently requires port-forwarding to interact with the pod within the cluster.**
  **To run using the kubernetes cluster, first install [k3d](https://k3d.io/v5.6.0/#what-is-k3d)**
    
