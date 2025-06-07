Projektidee

Ahrensburg.city Backup: Speichern, Verwalten und Wiederherstellen von XML-Inhalten ohne Nutzerdaten. Jeder kann die XML-Datei herunterladen, bearbeiten und auf der eigenen Homepage oder anderweitig verwenden.Voraussetzungen

Folgende Komponenten müssen installiert sein, damit die Datei ausgeführt werden kann:

* [MediaWiki 1.43](https://docs.google.com/document/d/1iARXk2GluegpHuMp-NSI0g-cOucYcFi6qWb9M2GyVWg/edit)

MediaWiki 1.43

* Unterstützt verschiedene Datenbanken wie MySQL, PostgreSQL, SQLite3 und weitere.

Installationsanleitung

Zur Installation von MediaWiki 1.43 sind die folgenden Befehle auszuführen:  
```
cd /var/www  
sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git /var/www/mediawiki  
cd mediawiki  
sudo git tag \-l | sort \-V  
sudo git checkout 1.39.11  
sudo git submodule update \--init \--recursive  
sudo chown \-R www-data:www-data /var/www/mediawiki  
sudo chmod \-R 755 /var/www/mediawiki
```