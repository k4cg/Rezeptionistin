# Rezeptionistin
Der freundliche IRC Bot für #k4cg

# Features

```
Erzaehl mir doch was du brauchst, mein Junge.
Ich kann bisher:
!gt - Guten Tag wuenschen.
!offen - Aktuelle Geraete in der K4CG anzeigen
fragen beantworten in Form: <soll/kann/darf/muss> ich * [<oder> *]
!schmeichle <nick> - Jemandem ein Kompliment machen.
!beleidige <nick> - Jemanden beleidigen.
!security - Aktuelle Sicherheitsprobleme im Internetz
!lang - Ändern die Sprache
!lineart - Zeige eine lineart
Mich beim freenode NickServ authentifizieren.
!offen - Aktuelle Geraete in der K4CG anzeigen lassen
!np - Dir sagen welche Musik so laeuft.
!sage <nick> <nachricht> - Einem Benutzer eine Nachricht ausrichten wenn er das naechste mal auftaucht.
!kt - Zeige aktuelle Temperatur in der K4CG.
```

# Installation

``` bash
git clone https://github.com/k4cg/Rezeptionistin
```

Nach dem Klonen müssen die Abhängigkeiten installiert, und eine config.ini Datei angelegt werden.

``` bash
cd rezeptionistin
pip install -r requirements.txt
cp config.ini.example config.ini
```

**! config.ini muss vor der Benutzung angepasst werden**

# Benutzung

``` bash
./rezeptionistin.py
```

# Konfiguration

Es wird automatisch die `config.ini` im gleichen Verzeichnis gelesen.

``` ini
[IRC]
server = irc.freenode.net
port = 6667
nick = Rezeptionistin
ircchan = #k4cg
debugchan = #k4cgdebug

[HTTP]
useragent = Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3

[MediaWiki]
wikiapiurl = https://k4cg.org/api.php
user = Rezeptionistin
password = passw0rd

[OpenStatus]
url = http://[2001:dead:beef::1]:80/status.json

[Language]
language = de
```

Optionen für Sprache: "de" oder "en"
