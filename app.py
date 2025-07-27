from flask import Flask, request, send_from_directory, Response
import os
import subprocess
import re

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

def _ping_command_parts(ip: str, os_name: str) -> list[str]:
    """Return the ping command parts for the given OS."""
    if os_name and os_name.lower() == "windows":
        flag = "-n"
    else:
        flag = "-c"
    return ["ping", flag, "1", ip]


@app.route('/vulnerable/ping')
def vulnerable_ping():
    ip = request.args.get('ip')
    os_name = request.args.get('os', 'linux')
    # Verwundbar: direkte Shell-Ausführung
    cmd_parts = _ping_command_parts(ip, os_name)
    cmd = " ".join(cmd_parts)
    try:
        proc = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return Response(proc.stdout.decode(errors="ignore"), mimetype="text/plain")
    except Exception as e:
        return Response(f"Fehler: {e}", status=500, mimetype="text/plain")

@app.route('/secure/ping')
def secure_ping():
    ip = request.args.get('ip')
    os_name = request.args.get('os', 'linux')
    if not ip:
        return Response("IP-Adresse fehlt", status=400)
    # Nur IPv4-Adressen erlauben
    if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ip):
        return Response("Ungültige IP-Adresse", status=400)
    try:
        cmd_parts = _ping_command_parts(ip, os_name)
        result = subprocess.run(
            cmd_parts,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=5,
        )
        encoding = "cp850" if os.name == "nt" else "utf-8"
        output = result.stdout.decode(encoding, errors="ignore")
        return Response(output, mimetype="text/plain")
    except Exception as e:
        return Response(f"Fehler: {str(e)}", status=500, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
