# Download
## Projektidee
Ahrensburg.city Backup: XML-Inhalte ohne Nutzerdaten speichern, verwalten und wiederherstellen.  
Die XML-Datei kann jeder herunterladen, bearbeiten und auf der eigenen Homepage oder anderswo verwenden.
## Voraussetzungen
Damit die Datei ausgeführt werden kann, müssen folgende Komponenten installiert sein:
* [MediaWiki 1.43](#mediawiki-143)


### MediaWiki 1.43
* Unterstützt verschiedene Datenbanken wie MySQL, PostgreSQL, SQLite3 und andere.

#### Installationsanleitung:
Führen Sie die folgenden Befehle aus, um MediaWiki 1.43 zu installieren:

```bash
cd /var/www
sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git /var/www/mediawiki
cd mediawiki
sudo git tag -l | sort -V
sudo git checkout 1.39.11
sudo git submodule update --init --recursive
sudo chown -R www-data:www-data /var/www/mediawiki
sudo chmod -R 755 /var/www/mediawiki
```
