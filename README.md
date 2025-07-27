# Command Injection Demo

Dieses kleine Projekt demonstriert eine typische OWASP Top 10 Schwachstelle: Command Injection.
Es stehen zwei Varianten zur Verfügung: eine verwundbare und eine sichere Implementierung.

## Voraussetzungen
* Python 3
* [Flask](https://flask.palletsprojects.com/) (`pip install flask`)

## Starten der Anwendung
```bash
python app.py
```
Die Anwendung lauscht dann auf `http://localhost:5000`.

## Bedienung
1. Rufen Sie im Browser `http://localhost:5000` auf.
2. Wählen Sie oben Ihr Betriebssystem (Linux/macOS oder Windows). Dadurch wird
   der passende `ping`-Befehl erzeugt.
3. Wählen Sie per Radiobutton die verwundbare oder sichere Version.
4. Geben Sie eine IP-Adresse ein und klicken Sie auf **Ping senden**.

### Verwundbare Version ausnutzen
* **Linux/macOS:** `127.0.0.1; ls`
* **Windows:** `127.0.0.1 & dir`

Die Ausgabe des zusätzlichen Kommandos wird im Textfeld angezeigt.

### Sichere Version
Hier wird die Eingabe validiert und ohne Shell ausgeführt. Der Versuch, weitere Befehle anzuhängen, führt zu einer Fehlermeldung.
Die Anwendung funktioniert sowohl unter Linux/macOS als auch unter Windows.\
Wählen Sie einfach oben das passende Betriebssystem aus, damit der korrekte
`ping`-Befehl verwendet wird.

## Funktionsweise
Die verwundbare Version führt das Kommando
```
ping -c 1 <ip>  # Linux/macOS
ping -n 1 <ip>  # Windows
```
direkt in der Shell aus. Dadurch k\u00f6nnen angehängte Befehle ausgeführt werden.

Die sichere Variante prüft die IP-Adresse mittels Regex
und übergibt das Kommando ohne Shell an `subprocess.run()`.
