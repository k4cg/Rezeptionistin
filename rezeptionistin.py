#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re
import time
import random
import socket
import string
import codecs
import urllib2
import ConfigParser
from plugin import Plugin
from wikitools import wiki
from vendor import importdir
from bs4 import BeautifulSoup
from wikitools import category
from asyncirc.ircbot import IRCBot

class Rezeptionistin(object):

  # Constructor
  #

  def __init__(self):

    # load config
    config = ConfigParser.ConfigParser()
    if not config.read("config.ini"):
      print "Error: your config.ini could not be read"
      exit(1)

    # load plugins
    importdir.do("plugins", globals())
    self.plugins = [module() for module in Plugin.__subclasses__()]

    self.server=config.get('IRC','server')
    self.port=int(config.get('IRC', 'port'))
    self.nick=config.get('IRC', 'nick')
    self.ircchan=config.get('IRC', 'ircchan')
    self.debugchan=config.get('IRC', 'debugchan')
    self.nickservpassword=config.get('IRC', 'nickservpassword')
    self.useragent=config.get('HTTP', 'useragent')
    self.site = wiki.Wiki(config.get('MediaWiki', 'wikiapiurl'))
    self.site.login(config.get('MediaWiki', 'user'), config.get('MediaWiki', 'password'))
    self.httpregex=re.compile(r'https?://')

    self.irc = IRCBot(self.server, self.port, self.nick)


  # Helper Methods
  #

  def netcat(self, hostname, port, content):
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

  def wikiupdate(self, title, url):
    cat = category.Category(self.site, "Linklist")
    for article in cat.getAllMembersGen(namespaces=[0]):
      print article.edit(appendtext="\n* {title} - {url} \n".format(title=title, url=url))

  def geturlfrommsg(self, message):
    url = re.search("(?P<url>https?://[^\s]+)", message).group("url")
    return url

  def getpage(self, url):
    req = urllib2.Request(url, headers={ 'User-Agent': self.useragent })
    soup = BeautifulSoup(urllib2.urlopen(req))
    return soup

  def geturltitle(self, url):
    try:
      page = self.getpage(url)
      title = self.sanitize(page.title.string.lstrip())
    except:
      title = ""
    return title

  def split_by_nth(self, text, n, seperator=' '):
    groups = text.split(seperator)
    res_l = list(seperator.join(groups[:n]))
    res_r = list(seperator.join(groups[n:]))
    res_l.extend(res_r)
    return res_l

  def send_message(self, recipient, msg):
    self.irc.msg(recipient, "\x0F" + msg)

  def send_command(self, recipient, cmd):
    self.irc.msg(recipient, cmd)

  def sanitize(self, s):
    return str(s).translate(string.maketrans("\n\r",'  '))


  # IRC Handlers

  def on_msg(self, irc, user_nick, host, channel, message):
    for plugin in self.plugins:
      plugin.on_msg(self, user_nick, host, channel, message)

  def on_privmsg(self, irc, user_nick, host, message):
    for plugin in self.plugins:
      plugin.on_privmsg(self, user_nick, host, message)

  def on_join(self, irc, user_nick, host, channel):
    for plugin in self.plugins:
      plugin.on_join(self, user_nick, host, channel)


  # Operations

  def run(self):
    # Assign event handlers
    self.irc.on_msg(self.on_msg)
    self.irc.on_privmsg(self.on_privmsg)
    self.irc.on_join(self.on_join)

    # Start Bot
    self.irc.start()
    self.irc.join(self.ircchan)
    self.irc.join(self.debugchan)

    # Run Eventloop
    try:
      while self.irc.running:
	time.sleep(1)
    except KeyboardInterrupt:
      print("Received exit command")
    finally:
      self.irc.stop()
