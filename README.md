wissen-ahrensburg.de Backup: XML-Inhalte werden ohne Nutzerdaten gespeichert, verwaltet und wiederhergestellt. Die XML-Datei steht zum Download bereit und kann bearbeitet sowie auf der eigenen Homepage oder anderweitig verwendet werden.

Voraussetzungen

- .NET 10 SDK installiert (https://dotnet.microsoft.com/)
- git installiert (https://git-scm.com/)

Projekt klonen
```bash
gh repo clone thorstenkloehn/Download  # oder
git clone https://github.com/thorstenkloehn/Download.git
sudo rm sicherung.xml
ssh hhhh@wissen-ahrensburg.de "cd /var/www/ahrensburgcity && sudo ./backup export /root/sicherung.xml --full"
scp jjjjj@wissen-ahrensburg.de:/root/sicherung.xml /home/thorsten/Downloads/sicherung.xml
```

