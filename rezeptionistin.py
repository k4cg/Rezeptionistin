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
from vendor import importdir
from bs4 import BeautifulSoup

from asyncirc.ircbot import IRCBot

class Rezeptionistin(object):

  # Constructor
  #

  def __init__(self):

    # load config
    self.config = ConfigParser.ConfigParser()
    self.translations = ConfigParser.ConfigParser()

    if not self.config.read("config.ini"):
      print "Error: your config.ini could not be read"
      exit(1)

    if not self.translations.read("language.ini"):
      print "Error: your language.ini could not be read"
      exit(1)

    # load plugins
    importdir.do("plugins", globals())
    self.plugins = [module(config=self.config) for module in Plugin.__subclasses__()]

    # load required config
    self.server=self.config.get('IRC','server')
    self.port=int(self.config.get('IRC', 'port'))
    self.nick=self.config.get('IRC', 'nick')
    self.ircchan=self.config.get('IRC', 'ircchan').split(",")
    self.useragent=self.config.get('HTTP', 'useragent')

    # load optional config
    try:
      self.nickservpassword=self.config.get('IRC', 'nickservpassword')
      self.debugchan=self.config.get('IRC', 'debugchan')
      self.language=self.config.get('Language','language')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
      pass

    # load config defaults
    if not hasattr(self, "language"):
      self.language = "de"

    self.identified = False
    self.httpregex = re.compile(r'https?://')
    self.irc = IRCBot(self.server, self.port, self.nick)


  # Helper Methods
  #

  def translate(self, language_key):
    return self.translations.get(self.language, language_key)

  def setlanguage(self, language):
    if not self.translations.has_section(language):
      return False

    self.language = language
    return True

  def getlanguage(self):
    return self.language

  def nickserv_identify():
    if not self.identified:
      self.identified = True
      if hasattr(self, "nickservpassword") and (self.ircchan == "#" + channel):
        self.send_command("NickServ", "identify " + self.nickservpassword)

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

  def geturlfrommsg(self, message):
    url = re.search("(?P<url>https?://[^\s]+)", message).group("url")
    return url

  def getpage(self, url):
    req = urllib2.Request(url, headers={ 'User-Agent': self.useragent })
    soup = BeautifulSoup(urllib2.urlopen(req),"html.parser")
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

  def get_plugin(self, name):
    for plugin in self.plugins:
      if type(plugin).__name__ == name:
        return plugin

  def check_user_authentication(self, user_nick, success_callback, failure_callback=None):
    authentication = self.get_plugin("Authentication")
    if authentication:
      authentication.check_user_authentication(self, user_nick, success_callback, failure_callback)

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

  def on_notice(self, irc, user_nick, host, channel, message):
    for plugin in self.plugins:
      plugin.on_notice(self, user_nick, host, channel, message[1:])


  # Operations

  def run(self):
    # Assign event handlers
    self.irc.on_msg(self.on_msg)
    self.irc.on_privmsg(self.on_privmsg)
    self.irc.on_join(self.on_join)
    self.irc.on_notice(self.on_notice)

    # Start Bot
    self.irc.start()
    for channel in self.ircchan:
      self.irc.join(channel)
    if hasattr(self, "debugchan"):
      self.irc.join(self.debugchan)

    # Run Eventloop
    try:
      while self.irc.running:
	time.sleep(1)
    except KeyboardInterrupt:
      print("Received exit command")
    finally:
      self.irc.stop()
