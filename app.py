# app.py
from flask import Flask
import psutil

app = Flask(__name__)

def get_cpu_usage():
    """Return CPU usage as a percentage."""
    return psutil.cpu_percent(interval=1)

@app.route('/')
def home():
    cpu = get_cpu_usage()
    return f"Infrastructure Monitoring Dashboard - CPU Usage: {cpu}%"

if __name__ == "__main__":
    print(f"Testing CPU usage: {get_cpu_usage()}%")
    app.run(debug=True)# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Infrastructure Monitoring Dashboard - Coming Soon!"

if __name__ == "__main__":
    app.run(debug=True)
