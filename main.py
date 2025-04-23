from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def run_simulation():
    try:
        # Using subprocess for better control over execution
        output = subprocess.check_output(["python", "simulation.py"], stderr=subprocess.STDOUT, text=True)
        return f"✅ Simulation executed successfully.\n\nOutput:\n{output}"
    except subprocess.CalledProcessError as e:
        return f"❌ Simulation failed.\n\nError:\n{e.output}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses this PORT environment variable
    app.run(host='0.0.0.0', port=port)
