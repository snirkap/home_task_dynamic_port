import os
import socket
import requests
from flask import Flask

app = Flask(__name__)

def register_service(port):
    service_registry_url = os.environ.get('SERVICE_REGISTRY_URL')
    pod_ip = os.environ.get('POD_IP')

    if service_registry_url and pod_ip:
        service_info = {'ip': pod_ip, 'port': port}
        etcd_key = f"/services/pod-two/{pod_ip}"
        etcd_url = f"{service_registry_url}/v2/keys{etcd_key}"

        response = requests.put(etcd_url, data={'value': str(port)})
        if response.status_code in [200, 201]:
            print(f"Registered service at {pod_ip}:{port}")
        else:
            print(f"Failed to register service: {response.text}")
    else:
        print("SERVICE_REGISTRY_URL or POD_IP not set")

@app.route('/')
def hello():
    return "Hello from Pod Two!"

if __name__ == '__main__':
    # Bind to port 0 to select an available port dynamically
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()

    register_service(port)

    app.run(host='0.0.0.0', port=port)
