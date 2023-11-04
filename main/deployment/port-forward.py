import subprocess
import time

# Retrieve the pod name dynamically using kubectl get
get_pod_name_command = [
    "kubectl",
    "get",
    "pods",
    "--selector=app=streamlit-llm",
    "--no-headers",
    "-o",
    "custom-columns=:metadata.name",
]
get_pod_name_process = subprocess.Popen(get_pod_name_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
pod_name, _ = get_pod_name_process.communicate()
if pod_name.strip():
    pod_name = pod_name.strip().decode()
    print(f"Found pod name: {pod_name}")

    # Run kubectl port-forward 
    port_forward_command = ["kubectl", "port-forward", f"pod/{pod_name}", "8501:8501"]
    port_forward_process = subprocess.Popen(port_forward_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        print("Trying to port forward to 8501. Stop the process when desired.")
        # Keep the script running and periodically check the status of the port-forwarding process
        while True:
            
            if port_forward_process.poll() is not None:
                print("Port forwarding process has terminated.")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (e.g., when you want to stop the script)
        print("Keyboard interrupt received. Stopping the port forwarding process.")
else:
    print("No pods found with the specified label selector.")