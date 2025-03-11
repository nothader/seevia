# app.py
from flask import Flask, jsonify
import psutil

app = Flask(__name__)

def get_cpu_usage():
    """Return CPU usage as a percentage."""
    return psutil.cpu_percent(interval=1)

@app.route('/')
def home():
    return "Infrastructure Monitoring Dashboard - Visit /metrics for data"

@app.route('/metrics')
def get_metrics():
    """Return system metrics as JSON."""
    cpu = get_cpu_usage()
    data = {'cpu': cpu}
    return jsonify(data)

if __name__ == "__main__":
    print(f"Testing CPU usage: {get_cpu_usage()}%")
    app.run(debug=True)
