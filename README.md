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

==LocalSettings==

```
define("NS_SCHWACHSTELLEN", 3006);
define("NS_SCHWACHSTELLEN_TALK", 3007);
$wgExtraNamespaces[NS_SCHWACHSTELLEN] = "Schwachstellen";
$wgExtraNamespaces[NS_SCHWACHSTELLEN_TALK] = "Schwachstellen Diskussion";
$wgNamespacesWithSubpages[NS_SCHWACHSTELLEN] = true;

// VisualEditor für Schwachstellen-Namensraum aktivieren
$wgVisualEditorAvailableNamespaces[NS_SCHWACHSTELLEN] = true;
$wgVisualEditorAvailableNamespaces[NS_SCHWACHSTELLEN_TALK] = true;
// Server-Namensraum
define("NS_SERVER", 3000);
define("NS_SERVER_TALK", 3001);
$wgExtraNamespaces[NS_SERVER] = "Server";
$wgExtraNamespaces[NS_SERVER_TALK] = "Server Diskussion";
$wgNamespacesWithSubpages[NS_SERVER] = true;

// Kurse-Namensraum
define("NS_KURSE", 3002);
define("NS_KURSE_TALK", 3003);
$wgExtraNamespaces[NS_KURSE] = "Kurse";
$wgExtraNamespaces[NS_KURSE_TALK] = "Kurse Diskussion";
$wgNamespacesWithSubpages[NS_KURSE] = true;


// AI-Namensraum
define("NS_AI", 3004);
define("NS_AI_TALK", 3005);
$wgExtraNamespaces[NS_AI] = "Ai";
$wgExtraNamespaces[NS_AI_TALK] = "Ai Diskussion";
$wgNamespacesWithSubpages[NS_AI] = true;

// VisualEditor für die neuen Namensräume aktivieren
$wgVisualEditorAvailableNamespaces[NS_SERVER] = true;
$wgVisualEditorAvailableNamespaces[NS_SERVER_TALK] = true;
$wgVisualEditorAvailableNamespaces[NS_KURSE] = true;
$wgVisualEditorAvailableNamespaces[NS_KURSE_TALK] = true;
$wgVisualEditorAvailableNamespaces[NS_AI] = true;
$wgVisualEditorAvailableNamespaces[NS_AI_TALK] = true;

define("NS_IDE", 3008);
define("NS_IDE_TALK", 3009);
$wgExtraNamespaces[NS_IDE] = "IDE";
$wgExtraNamespaces[NS_IDE_TALK] = "IDE Diskussion";
$wgNamespacesWithSubpages[NS_IDE] = true;
$wgVisualEditorAvailableNamespaces[NS_IDE] = true;
$wgVisualEditorAvailableNamespaces[NS_IDE_TALK] = true;
define("NS_BUILDER", 3010);
define("NS_BUILDER_TALK", 3011);

$wgExtraNamespaces[NS_BUILDER] = "Builder";
$wgExtraNamespaces[NS_BUILDER_TALK] = "Builder_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_BUILDER;
define("NS_BACKUP", 3012);
define("NS_BACKUP_TALK", 3013);

$wgExtraNamespaces[NS_BACKUP] = "Backup";
$wgExtraNamespaces[NS_BACKUP_TALK] = "Backup_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_BACKUP;




