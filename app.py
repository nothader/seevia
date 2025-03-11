# app.py
from flask import Flask, jsonify, render_template
import psutil

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
    print(f"Testing metrics - CPU: {get_cpu_usage()}%, Memory: {get_memory_usage()}%, Disk: {get_disk_usage()}%")
    app.run(debug=True)
