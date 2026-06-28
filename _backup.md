#!/bin/bash

# Sorgt dafür, dass das Skript bei Fehlern sofort abbricht
set -e

# Variablen definieren
username="xxx" # Definiert den Benutzernamen für die SSH-Verbindung auf dem Remote-Server.
server="xxx.de" # Definiert den Hostnamen oder die IP-Adresse des Remote-Servers, mit dem eine Verbindung hergestellt werden soll.
local_dir="/home/thorsten/Download" # Definiert den lokalen Verzeichnispfad, in dem die Sicherungsdateien gespeichert und verwaltet werden.
backup_file="sicherung.xml" # Definiert den Namen der Sicherungsdatei, die erstellt und übertragen wird.

# 1. Zuerst in das lokale Verzeichnis wechseln
echo "Wechsle in das lokale Verzeichnis..."
cd "$local_dir" || exit 1

# 2. Lokales Repository aktualisieren
echo "Aktualisiere Git-Repository..."
git pull

# 3. Alte Sicherung lokal löschen
echo "Lösche alte lokale Sicherung..."
rm -f "$backup_file"

# 4. Neues Backup auf dem Server erstellen
echo "Erstelle neues Backup auf dem Server..."
ssh "$username@$server" "cd /var/www/ahrensburgcity && ./backup export /tmp/$backup_file --full"

# 5. Backup vom Server herunterladen (und danach auf dem Server aufräumen)
echo "Lade Backup herunter..."
scp "$username@$server:/tmp/$backup_file" "$local_dir/$backup_file"
ssh "$username@$server" "rm -f /tmp/$backup_file"

# 6. Backup in Git sichern
echo "Backup in Git stagen..."
git add "$backup_file"

# Prüfen, ob es überhaupt Änderungen gibt, um leere Commits zu vermeiden
if git diff-index --quiet HEAD --; then
    echo "Keine Änderungen im Backup festgestellt. Kein Commit notwendig."
else
    echo "Änderungen erkannt. Committe Backup..."
    git commit -m "Backup vom $(date '+%Y-%m-%d %H:%M')"
    
    echo "Pushe zu Remote-Repository..."
    git push
fi

echo "Backup-Vorgang erfolgreich abgeschlossen!"