# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Infrastructure Monitoring Dashboard - Coming Soon!"

if __name__ == "__main__":
    app.run(debug=True)
