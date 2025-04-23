from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def run_simulation():
    try:
        output = subprocess.check_output(
            ["python", "simulation.py"], stderr=subprocess.STDOUT, text=True
        )
        return f"<pre>✅ Simulation executed:\n\n{output}</pre>"
    except subprocess.CalledProcessError as e:
        return f"<pre>❌ Simulation failed:\n\n{e.output}</pre>", 500
    except Exception as ex:
        return f"<pre>🔥 Unexpected error:\n{str(ex)}</pre>", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
