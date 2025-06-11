Ahrensburg.city Backup: XML-Inhalte werden ohne Nutzerdaten gespeichert, verwaltet und wiederhergestellt. Die XML-Datei steht zum Download bereit und kann bearbeitet, auf der eigenen Homepage oder anderweitig verwendet werden.

Voraussetzungen:

Für die Ausführung der Datei sind folgende Komponenten erforderlich:

* MediaWiki 1.43 ([Link](https://docs.google.com/document/d/1iARXk2GluegpHuMp-NSI0g-cOucYcFi6qWb9M2GyVWg/edit))  
* Unterstützung verschiedener Datenbanken wie MySQL, PostgreSQL, SQLite3 und mehr.

Installationsanleitung: (Hinweis: Installationsanleitung fehlt im Originaltext)

## wiki.ahrensburg.city

Dieses Wiki dient dazu, Meta-Projekte zu sammeln und zu beschreiben.

Zur Installation von MediaWiki 1.43 sind die folgenden Befehle auszuführen:

`cd /var/www`    
`sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git /var/www/mediawiki`    
`cd mediawiki`    
`sudo git tag \-l | sort \-V`    
`sudo git checkout 1.43.1`    
`sudo git submodule update \--init \--recursive`    
`sudo chown \-R www-data:www-data /var/www/mediawiki`    
`sudo chmod \-R 755 /var/www/mediawiki`

## 

## alterwiki.ahrensburg.city

Dieses Archiv enthält eine Sammlung alter Projekte und damit verbundenen Altlasten.

`cd /var/www`    
`sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git /var/www/alterwiki`   
`cd alterwiki`    
`sudo git tag \-l | sort \-V`    
`sudo git checkout 1.43.1`    
`sudo git submodule update \--init \--recursive`    
`sudo chown \-R www-data:www-data /var/www/alterwiki`    
`sudo chmod \-R 755 /var/www/alterwiki`  
`cd /var/www/alterwiki`  
`sudo COMPOSER=composer.local.json composer require --no-update mediawiki/semantic-media-wiki`  
`sudo composer update --no-dev`  
`COMPOSER=composer.local.json composer require --no-update mediawiki/maps`  
`composer update mediawiki/maps --no-dev -o`  
`php maintenance/update.php`

## stadtwiki.ahrensburg.city

Alle Informationen zum Thema Ahrensburg.

`cd /var/www`    
`sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git /var/www/stadtwiki`   
`cd   stadtwiki`  
`sudo git tag \-l | sort \-V`    
`sudo git checkout 1.43.1`    
`sudo git submodule update \--init \--recursive`    
`sudo chown \-R www-data:www-data /var/www/stadtwiki`  
`sudo chmod \-R 755 /var/www/stadtwiki`  
`cd /var/www/stadtwiki`  
`sudo COMPOSER=composer.local.json composer require --no-update mediawiki/semantic-media-wiki`  
`sudo composer update --no-dev`  
`COMPOSER=composer.local.json composer require --no-update mediawiki/maps`  
`composer update mediawiki/maps --no-dev -o`  
`php maintenance/update.php`

ahrensburg.city  
Ahrensburg  Portal
