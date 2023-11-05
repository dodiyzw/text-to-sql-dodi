# text-to-sql using LLM

## Summary

Motivated by the desire to investigate what Large Language Model (LLM) can do for us, this project attempts to apply one of (Hugging Face's)[https://huggingface.co] open source LLM model to take in text input from user and returns a SQL command output through a chatbot interface, similar to Chat-GPT. 

We often need to interact with databases in a corporate setting. LLM can supplement this process, especially for non-technical users that needs to query and retrieve certain data, but may not have the necessary domain knowledge yet to do so. 

While Chat-GPT is openly accessible right now, the OpenAI GPT-3.5 model API is not free for use. On the other hand, Hugging Face has made a plethora of models available open-sourced, and it can be easily implemented using Python. This app does not require any API key.



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



## Limitation and Future Improvements

  - While I have selected a relatively compressed LLM model, running the query still put substantial memory pressure on my local machine ( M1 Macbook Pro, 16GB RAM ). Future improve could consider hosting it in the cloud with more memory availability to avoid overwhelming local machines.

  - The deployment process as of now is not smooth, as it requires port-forwarding to access the service deployed on the kubernetes cluster. It would be better to see if there are ways to expose the service that can be defined using a config script. Once this setup is available, it can then be deployed to the cloud (i.e. AWS) and make it accesible to the public.

  - The queries were tested by myself, which may introduce a bias as I have some prior experience writing SQL queries, and may not be representative of the ability of this project to support non-technical users in writing SQL queries. More feedback will need to be gathered. 
