import os
import requests
import time

def discover_service():
    service_registry_url = os.environ.get('SERVICE_REGISTRY_URL')
    print(f"SERVICE_REGISTRY_URL: {service_registry_url}")  # Log the environment variable

    if service_registry_url:
        etcd_url = f"{service_registry_url}/v2/keys/services/pod-two"
        print(f"Querying etcd at: {etcd_url}")  # Log the etcd URL
        try:
            response = requests.get(etcd_url)
            print(f"etcd response status: {response.status_code}")  # Log the response status
            if response.status_code == 200:
                node = response.json().get('node', {})
                nodes = node.get('nodes', [])
                if nodes:
                    service_node = nodes[0]
                    ip = service_node['key'].split('/')[-1]
                    port = service_node['value']
                    print(f"Discovered Pod Two at {ip}:{port}")  # Log the discovered IP and port
                    return ip, port
                else:
                    print("No registered instances of Pod Two found.")
            else:
                print(f"Failed to retrieve service info: {response.status_code} {response.text}")
        except Exception as e:
            print(f"Exception while querying etcd: {e}")
    else:
        print("SERVICE_REGISTRY_URL not set")
    return None, None

def communicate_with_pod_two(ip, port):
    url = f"http://{ip}:{port}/"
    print(f"Communicating with Pod Two at {url}")  # Log the communication attempt
    try:
        response = requests.get(url)
        print(f"Response from Pod Two: {response.text}")
    except Exception as e:
        print(f"Error communicating with Pod Two at {ip}:{port} - {e}")

if __name__ == '__main__':
    print("Starting client.py")  # Log the start of the script
    while True:
        ip, port = discover_service()
        if ip and port:
            communicate_with_pod_two(ip, port)
        else:
            print("Could not discover Pod Two")
        time.sleep(10)  # Wait for 10 seconds before retrying
