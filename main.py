from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def run_simulation():
    os.system('python simulation.py')
    return "✅ Simulation executed. Check logs/output."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
