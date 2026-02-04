Ahrensburg.city Backup: XML-Inhalte werden ohne Nutzerdaten gespeichert, verwaltet und wiederhergestellt. Die XML-Datei steht zum Download bereit und kann bearbeitet, auf der eigenen Homepage oder anderweitig verwendet werden.

Voraussetzungen:

Für die Ausführung der Datei sind folgende Komponenten erforderlich:

* MediaWiki 1.43 ([Link](https://docs.google.com/document/d/1iARXk2GluegpHuMp-NSI0g-cOucYcFi6qWb9M2GyVWg/edit))  
* Unterstützung verschiedener Datenbanken wie MySQL, PostgreSQL, SQLite3 und mehr.

Installationsanleitung: (Hinweis: Installationsanleitung fehlt im Originaltext)

## Auf Entwicklungsserver installieren

**Hinweis:** Die folgenden Schritte gelten ausschließlich für Entwicklungsserver und sollten nicht auf Produktivsystemen verwendet werden.

1. Voraussetzungen prüfen und sicherstellen, dass alle benötigten Komponenten installiert sind (z.B. PHP, Webserver, Datenbank).
2. Repository klonen und MediaWiki installieren (siehe Befehle unten).
3. Konfiguration und Anpassungen können auf dem Entwicklungsserver getestet werden, bevor Änderungen in eine Produktionsumgebung übernommen werden.
4. Sicherheitsaspekte wie Benutzerrechte und Zugangsbeschränkungen beachten, da Entwicklungsserver nicht für den produktiven Einsatz gedacht sind.
```
`cd /var/www`    
`sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git /var/www/mediawiki`    
`cd mediawiki`    
`sudo git tag \-l | sort \-V`    
`sudo git checkout 1.43.1`    
`sudo git submodule update \--init \--recursive`    
`sudo chown \-R www-data:www-data /var/www/mediawiki`    
`sudo chmod \-R 755 /var/www/mediawiki`
```
start

## LocalSettings

```
wfLoadExtension( 'CategoryTree' );
wfLoadExtension( 'SyntaxHighlight_GeSHi' );
wfLoadExtension( 'VisualEditor' );
# Cookie-Warnung aktivieren
wfLoadExtension( 'CookieWarning' );
wfLoadExtension( 'SyntaxHighlight_GeSHi' );
wfLoadExtension( 'intersection' );
$wgCookieWarningEnabled=true;
$wgCookieWarningMoreUrl='';
$wgCookieWarningGeoIPServiceURL='';
$wgCookieWarningGeoIPLookup='none';
$wgCookieWarningForCountryCodes="EU";
define("NS_Nachrichten", 3000);
define("NS_Nachrichten_TALK", 3001);

$wgExtraNamespaces[NS_Nachrichten] = "Nachrichten";
$wgExtraNamespaces[NS_Nachrichten_TALK] = "Nachrichten_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_Nachrichten;
```
