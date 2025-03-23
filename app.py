# Launch app.py
from flask import Flask, jsonify, render_template
import psutil
import argparse

app = Flask(__name__)

def get_cpu_usage():
    """Return CPU usage as a percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Return memory usage as a percentage."""
    return psutil.virtual_memory().percent

def get_disk_usage():
    """Return disk usage as a percentage for the root directory."""
    return psutil.disk_usage('/').percent

@app.route('/')
def home():
    """Render the dashboard homepage."""
    return render_template('index.html')

@app.route('/metrics')
def get_metrics():
    """Return system metrics as JSON."""
    data = {
        'cpu': get_cpu_usage(),
        'memory': get_memory_usage(),
        'disk': get_disk_usage()
    }
    return jsonify(data)

if __name__ == "__main__":
    # Set up CLI arguments
    parser = argparse.ArgumentParser(description="Infrastructure Monitoring Dashboard")
    parser.add_argument('--host', default='127.0.0.1', help="Host to run the app on (default: 127.0.0.1)")
    parser.add_argument('--port', type=int, default=5000, help="Port to run the app on (default: 5000)")
    args = parser.parse_args()

    # Print test metrics and run the app
    print(f"Testing metrics - CPU: {get_cpu_usage()}%, Memory: {get_memory_usage()}%, Disk: {get_disk_usage()}%")
    app.run(host=args.host, port=args.port, debug=True)
