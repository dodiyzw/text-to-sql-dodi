#! /bin/bash
k3d cluster create streamlit-llm 

kubectl apply -f streamlit-manifest.yaml

echo "Waiting for container to start"
sleep 20 # give some time for container to start
# temporary solution: we will port forward.

while true; do
    # Get the pod's status
    podName=$(kubectl get pods --selector=app=streamlit-llm --no-headers -o custom-columns=:metadata.name)
    podStatus=$(kubectl get pod "$podName" --no-headers -o custom-columns=:status.phase)

    if [ "$podStatus" == "Running" ]; then
        echo " >>> Pod is Running, port forwarding to 8501... <<< "
        kubectl port-forward "$podName" 8501:8501
        break 
    else
        echo "Pod is not in the Running state (Current status=$podStatus). Waiting and checking again..."
        sleep 10 # Wait for 5 seconds before checking the status again
    fi
done