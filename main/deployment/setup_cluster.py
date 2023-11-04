import subprocess
import time
# Create a k3d cluster
print("Creating cluster...")
k3d_create_command = ["k3d", "cluster", "create", "streamlit-llm"]
k3d_process = subprocess.Popen(k3d_create_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
k3d_process.wait()

# Apply a Kubernetes manifest
print("Applying manifest")
kubectl_apply_command = ["kubectl", "apply", "-f", "streamlit-manifest.yaml"]
kubectl_process = subprocess.Popen(kubectl_apply_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
kubectl_process.wait()

# Optionally, check the exit codes of the processes to handle errors or log results
if k3d_process.returncode == 0:
    print("k3d cluster created successfully.")
else:
    print(f"Error creating k3d cluster: {k3d_process.stderr.read().decode()}")

if kubectl_process.returncode == 0:
    print("Kubernetes manifest applied successfully.")
else:
    print(f"Error applying Kubernetes manifest: {kubectl_process.stderr.read().decode()}")

