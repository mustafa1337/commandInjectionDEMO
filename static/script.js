function ping() {
  const ip = document.getElementById('ip').value;
  const output = document.getElementById('output');
  const mode = document.querySelector('input[name="mode"]:checked').value;
  const osName = document.getElementById('os').value;
  const endpoint = mode === 'vulnerable' ? '/vulnerable/ping' : '/secure/ping';

  output.textContent = 'Sende Anfrage...';

  fetch(`${endpoint}?ip=${encodeURIComponent(ip)}&os=${encodeURIComponent(osName)}`)
    .then(res => res.text())
    .then(data => {
      output.textContent = data;
    })
    .catch(err => {
      output.textContent = 'Fehler: ' + err;
    });
}
