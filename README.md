# Rezeptionistin
Der freundliche IRC Bot für #k4cg

# Features

* `!gt` - PING Hello Nachricht, mit nick
* `!kt` - Zeige aktuelle Temperatur in der K4CG
* `!help` - Zeige Hilfe, antwort im Query
* URL Title - Fetcht den Titel von http(s) links und postet den inhalt in den Channel #k4cg

# Usage

``` bash
git clone https://github.com/k4cg/Rezeptionistin
cd rezeptionistin
./rezeptionistin.py
```

# Configuration

Einfach nur interne Variablen benutzen im Skript.

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
```
