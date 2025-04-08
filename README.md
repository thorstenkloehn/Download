# Download
## Projektidee
Ahrensburg.city Backup: XML-Inhalte ohne Nutzerdaten speichern, verwalten und wiederherstellen.  
Die XML-Datei kann jeder herunterladen, bearbeiten und auf der eigenen Homepage oder anderswo verwenden.
## Voraussetzungen
Damit die Datei ausgeführt werden kann, müssen folgende Komponenten installiert sein:
* [MediaWiki 1.43](#mediawiki-143)
* [Composer](#Composer)
* [Maps](#Maps)
* [Semantic Web]()

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

### Composer
Führen Sie die folgenden Befehle aus, um Composer in einer Version über 2.0 zu installieren:
```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'dac665fdc30fdd8ec78b38b9800061b4150413ff2e3b6f88543c636f7cd84f6db9189d43a81e5503cda447da73c7e5b6') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"

sudo mv composer.phar /usr/local/bin/composer
```

### Maps
Führen Sie die folgenden Befehle aus, um die Maps-Erweiterung zu installieren:
```bash
cd /var/www/mediawiki
COMPOSER=composer.local.json composer require --no-update mediawiki/maps
composer update mediawiki/maps --no-dev -o
```

### Semantic Web
Führen Sie die folgenden Befehle aus, um die Semantic Web-Erweiterung zu installieren:
```bash
cd /var/www/mediawiki
sudo COMPOSER=composer.local.json composer require --no-update mediawiki/semantic-media-wiki
sudo composer update --no-dev
php maintenance/update.php
```

### Konfiguration
Führen Sie die folgenden Befehle aus:
```bash
sudo nano /var/www/mediawiki/LocalSettings.php
```
Fügen Sie den folgenden Text hinzu:

```php
wfLoadExtension( 'SemanticResultFormats' );



wfLoadExtension( 'SemanticMediaWiki' );
enableSemantics( 'Ihre Homepage-Adresse' );
wfLoadExtension( 'Maps' );
semantic-result-formats
$egMapsDefaultService = 'leaflet';
```
### Jetzt können Sie das Git-Projekt herunterladen

Führen Sie den folgenden Befehl aus, um das Projekt von GitHub zu klonen und ausführen:

```bash
git clone https://github.com/thorstenkloehn/Download.git /Download
php /var/www/mediawiki/maintenance/run.php importDump.php < /Download/pagedump.xml
```
### Bei Fehlern besuchen Sie bitte die folgenden Seiten:

* [SemanticMediaWiki](https://www.semantic-mediawiki.org/)
* [MediaWiki](https://www.mediawiki.org/)
* [Maps](https://www.mediawiki.org/wiki/Extension:Maps)
### Weitere Erweiterungen werden noch benötigt
#### Composer 
##### Semantic Result Formats
```bash
cd /var/www/mediawiki
sudo COMPOSER=composer.local.json composer require --no-update mediawiki/semantic-result-formats
sudo composer update --no-dev
```
```
nano /var/www/mediawiki/LocalSettings.php
wfLoadExtension( 'SemanticResultFormats' );
```
##### Mermaid
```bash
cd /var/www/mediawiki
sudo COMPOSER=composer.local.json composer require --no-update mediawiki/mermaid
sudo composer update --no-dev
```
```
nano /var/www/mediawiki/LocalSettings.php
wfLoadExtension( 'Mermaid' );  
$mermaidgDefaultTheme = 'neutral';
```
### wget
```
sudo rm -R /thorsten
mkdir /thorsten
sudo chmod 777 -R thorsten
cd /thorsten
wget https://extdist.wmflabs.org/dist/extensions/CookieWarning-REL1_43-f697459.tar.gz
tar -xzf CookieWarning-REL1_43-f697459.tar.gz -C /var/www/mediawiki/extensions
wget https://extdist.wmflabs.org/dist/extensions/YouTube-REL1_43-01673ce.tar.gz
tar -xzf YouTube-REL1_43-01673ce.tar.gz -C /var/www/mediawiki/extensions
wget https://extdist.wmflabs.org/dist/extensions/MobileFrontend-REL1_43-9de9f8b.tar.gz
tar -xzf MobileFrontend-REL1_43-9de9f8b.tar.gz -C /var/www/mediawiki/extensions
```
```
nano /var/www/mediawiki/LocalSettings.php
wfLoadExtension( 'YouTube' );
$wgCookieWarningEnabled=true;
$wgCookieWarningMoreUrl='';
$wgCookieWarningGeoIPServiceURL='';
$wgCookieWarningGeoIPLookup='none';
$wgCookieWarningForCountryCodes="EU";
wfLoadExtension( 'CookieWarning' );
wfLoadExtension( 'Gadgets' );
wfLoadExtension( 'SyntaxHighlight_GeSHi' );
$wgDefaultMobileSkin = 'minerva'; // verwende den Minerva-Skin (Du musst ihn in 1.
$wgDefaultMobileSkin = 'vector'; // verwende den Vector-Ski
$wgDefaultMobileSkin = 'timeless'; // verwende den Timeless-Skin

```


