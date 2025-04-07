# Download
## Voraussetzungen
Damit die Datei ausgeführt werden kann, müssen folgende Komponenten installiert sein:
* [MediaWiki 1.43](#mediawiki-143)
* [Composer](#Composer)
* Maps
* Semantic Web
### MediaWiki 1.43
* Unterstützt verschiedene Datenbanken wie MySQL, PostgreSQL, SQLite3 und andere.

#### Installationsanleitung:
Führen Sie die folgenden Befehle aus, um MediaWiki 1.43 zu installieren:

```bash
cd /var/www
sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git mediawiki
cd mediawiki
sudo git tag -l | sort -V
sudo git checkout 1.43.0
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

```
cd /var/www/mediawiki
COMPOSER=composer.local.json composer require --no-update mediawiki/maps
composer update mediawiki/maps --no-dev -o
```





