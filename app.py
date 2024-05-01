import os
from flask import Flask
from kubernetes import client, config

app = Flask(__name__)

@app.route('/')
def home():
    config.load_incluster_config()
    v1 = client.CoreV1Api()
    pod_name = os.getenv('MY_POD_NAME')
    pod_namespace = os.getenv('MY_POD_NAMESPACE')
    pod = v1.read_namespaced_pod(name=pod_name, namespace=pod_namespace)
    node_name = pod.spec.node_name
    pod_ip = pod.status.pod_ip
    return f"Pod Name: {pod_name}, Node Name: {node_name}, Pod Namespace: {pod_namespace}, Pod IP: {pod_ip}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
