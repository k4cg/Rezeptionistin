# coding: utf8

import socket
import urllib2
import json
from plugin import Plugin

class Temperature(Plugin):

  def __init__(self, config=None):
    try:
      self.wunderground = config.get('Temperature', 'wunderground')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
      print "Temperature was not properly configured in your config.ini"
    super(Temperature, self).__init__()

  def help_text(self, bot):
    return bot.translate("temp_help")

  def get_indoor_temp(self, bot):
    msg = bot.get_spacestatus_data()
    temp = str(msg['temp'])
    return temp

  def get_outdoor_temp(self, bot):
    f = urllib2.urlopen(self.wunderground)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    temp_outdoor = parsed_json['current_observation']['temp_c']
    f.close()
    return temp_outdoor

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!kt'):
      temp = self.get_indoor_temp(bot)
      temp_outdoor = self.get_outdoor_temp(bot)

      if temp is not "":
          bot.send_message(channel, bot.translate("temp_str1").format(temp=temp) + " " + bot.translate("temp_str2").format(temp=temp_outdoor), user_nick)
      else:
          bot.send_message(channel, bot.translate("temp_str3").format(temp=temp_outdoor), user_nick)

  def on_privmsg(self, bot, user_nick, host, message):
    if message.lower().startswith('!kt'):
      temp = self.get_indoor_temp(bot)
      temp_outdoor = self.get_outdoor_temp(bot)

      if temp is not "":
          bot.send_message(user_nick, bot.translate("temp_str1").format(temp=temp) + " " + bot.translate("temp_str2").format(temp=temp_outdoor), user_nick)
      else:
          bot.send_message(user_nick, bot.translate("temp_str3").format(temp=temp_outdoor), user_nick)
