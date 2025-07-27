from flask import Flask, request, send_from_directory
import os
import subprocess
import re

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

def _ping_command(ip: str, os_name: str) -> str:
    """Create the ping command for the given OS."""
    if os_name.lower() == "windows":
        flag = "-n 1"
    else:
        flag = "-c 1"
    return f"ping {flag} {ip}"


@app.route('/vulnerable/ping')
def vulnerable_ping():
    ip = request.args.get('ip')
    os_name = request.args.get('os', 'linux')
    # Verwundbar: direkte Shell-Ausführung
    cmd = _ping_command(ip, os_name)
    result = os.popen(cmd).read()
    return result

@app.route('/secure/ping')
def secure_ping():
    ip = request.args.get('ip')
    os_name = request.args.get('os', 'linux')
    # Nur IPv4-Adressen erlauben
    if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ip):
        return "Ungültige IP-Adresse", 400
    try:
        cmd = _ping_command(ip, os_name).split()
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout
    except Exception as e:
        return f"Fehler: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
