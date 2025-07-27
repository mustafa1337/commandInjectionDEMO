# Command Injection Demo

Dieses kleine Projekt demonstriert eine typische OWASP Top 10 Schwachstelle: Command Injection.
Es stehen zwei Varianten zur Verf\u00fcgung: eine verwundbare und eine sichere Implementierung.

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
2. W\u00e4hlen Sie oben Ihr Betriebssystem (Linux/macOS oder Windows).
3. W\u00e4hlen Sie per Radiobutton die verwundbare oder sichere Version.
4. Geben Sie eine IP-Adresse ein und klicken Sie auf **Ping senden**.

### Verwundbare Version ausnutzen
* **Linux/macOS:** `127.0.0.1; ls`
* **Windows:** `127.0.0.1 & dir`

Die Ausgabe des zusätzlichen Kommandos wird im Textfeld angezeigt.

### Sichere Version
Hier wird die Eingabe validiert und ohne Shell ausgef\u00fchrt. Der Versuch, weitere Befehle anzuh\u00e4ngen, f\u00fchrt zu einer Fehlermeldung.

## Funktionsweise
Die verwundbare Version f\u00fchrt das Kommando
```
ping -c 1 <ip>  # Linux/macOS
ping -n 1 <ip>  # Windows
```
direkt in der Shell aus. \nDadurch k\u00f6nnen angeh\u00e4ngte Befehle ausgef\u00fchrt werden.

Die sichere Variante pr\u00fcft die IP-Adresse mittels Regex
und \u00fcbergibt das Kommando ohne Shell an `subprocess.run()`.

