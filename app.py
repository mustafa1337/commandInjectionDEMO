from flask import Flask, request, send_from_directory
import os
import subprocess
import re

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/vulnerable/ping')
def vulnerable_ping():
    ip = request.args.get('ip')
    # Verwundbar: direkte Shell-Ausführung
    result = os.popen(f"ping -c 1 {ip}").read()
    return result

@app.route('/secure/ping')
def secure_ping():
    ip = request.args.get('ip')
    # Nur IPv4-Adressen erlauben
    if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ip):
        return "Ungültige IP-Adresse", 400
    try:
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout
    except Exception as e:
        return f"Fehler: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
