#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
from asyncirc.ircbot import IRCBot
import sys
import socket
import re
import urllib2
from bs4 import BeautifulSoup

server="irc.freenode.net"
port=6667
nick="Rezeptionistin"
ircchan="#k4cg"
debugchan="#k4cgdebug"
useragent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3'
httpregex=re.compile(r'https?://')

if sys.hexversion > 0x03000000:
    raw_input = input

logging.basicConfig(level=logging.DEBUG)
irc = IRCBot(server, port, nick)

# Custom Functions
def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.shutdown(socket.SHUT_WR)
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        f = data
    s.close()
    return f

def geturltitle(message):
    try:
        url = re.search("(?P<url>https?://[^\s]+)", message).group("url")
        req = urllib2.Request(url, headers={ 'User-Agent': useragent })
        soup = BeautifulSoup(urllib2.urlopen(req))
        t = soup.title.string
	t = t.lstrip()
        t = t.encode('ascii','ignore')
    except:
        t = ""
    return t

def send_message(self, recipient, msg):
    self.msg(recipient, ":\x0F" + msg)
def send_command(self, recipient, cmd):
    self.msg(recipient, ":" + cmd)

# IRC Handlers

@irc.on_msg
def on_msg(self, nick, host, channel, message):
    if message.lower().startswith('!help'):
        send_message(self, nick, "Erzaehl mir doch was du brauchst, mein Junge.")
        send_message(self, nick, "Ich kann bisher:")
        send_message(self, nick, "!kt - Zeige aktuelle Temperatur in der K4CG.")
        send_message(self, nick, "!gt - Guten Tag wuenschen.")
        send_message(self, nick, "!np - Dir sagen welche Musik so laeuft.")
        send_message(self, nick, "oder dir den Titel von URLs sagen die du in den Channel postest")
    if message.lower().startswith('!kt'):
        temp = netcat("2001:a60:f073:0:21a:92ff:fe50:bdfc", 31337, "9001")
        send_message(self, channel, "Die aktuelle Temeratur in der K4CG ist{temp} Grad".format(temp=temp) )
    if message.lower().startswith('!gt'):
        send_message(self, channel, "Ich lebe noch, {nick}".format(nick=nick))
    if message.lower().startswith('!np'):
        send_message(self, channel, "Das funktioniert noch nicht.")
    if httpregex.search(message.lower()) is not None:
        title = geturltitle(message)
        if not title == "":
            send_message(self, channel, "Title: {title}".format(title=title))

@irc.on_privmsg
def on_privmsg(self, nick, host, message):
    if message.lower().startswith('!gt'):
        send_message(self, nick, "Ich lebe noch, {nick}".format(nick=nick))

# Start Bot
irc.start()
irc.join(ircchan)
irc.join(debugchan)

# Run Eventloop
try:
    while irc.running:
        irc.send_raw(raw_input(""))
except KeyboardInterrupt:
    print("Received exit command")
finally:
    irc.stop()
