# Infrastructure Monitoring Dashboard

A Python-based tool to visualize system metrics (CPU, memory, disk) in a web dashboard.

## Setup
1. Clone the repo: `git clone https://github.com/nothader/seevia`
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `python app.py`

## Features
- Real-time charts for CPU, memory, and disk usage, updating every 2 seconds.
- Configurable host and port via CLI.

## Usage
- Visit `/` for the dashboard homepage (HTML).
- Fetch metrics at `/metrics` (returns JSON).
- Run with custom settings: `python app.py --host 0.0.0.0 --port 8080`
- See options: `python app.py --help`

## Status
- [x] Project setup
- [x] Collect system metrics (CPU, memory, disk)
- [x] Display charts
- [x] Add CLI options
