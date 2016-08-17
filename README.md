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

[Temperature]
host = 2001:a60:f073:0:21d:92ff:fe25:2a23
port = 31337
wunderground = http://api.wunderground.com/api/a5744ceb15b96090/conditions/q/pws:INUREMBE2.json

[Sentences]
satzgenerator = off
markov = on
markovfile = /usr/local/rezeptionistin/corpus.txt
```

Optionen für Sprache: "de" oder "en"

# Sentences

Wenn man den Bot im Chat mit "Rezeptionistin" anspricht, wird das Sentences
Plugin getriggered. Dieses Antwortet mit einem zufaellgiem Satz darauf.

Dieser Satz kann aus zwei Quellen kommen. Entweder `markov` oder
`satzgenerator`. Satzgenerator ist eine Site im Netz die man per API
anfragen kann. Der Markov Teil nutzt den Markov-Chain Algo und einen Corpus
den man vorher angeben muss.

Wenn beide (`satzgenerator` und `markov`) angeschaltet sind, wird eine
zufaellige Quelle ausgewaehlt.

