# coding: utf8

import socket
import urllib2
import json
from plugin import Plugin

class Temperature(Plugin):
  def help_text(self, bot):
    return bot.translate("temp_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!kt'):
      temp = bot.netcat("2001:a60:f073:0:21d:92ff:fe25:2a23", 31337, "9001").strip()
      
      station_id = "INUREMBE2";
      f = urllib2.urlopen('http://api.wunderground.com/api/a5744ceb15b96090/conditions/q/pws:' + station_id + '.json')
      json_string = f.read()
      parsed_json = json.loads(json_string)
      temp_outdoor = parsed_json['current_observation']['temp_c']
      f.close()
      
      if temp is not "":
          bot.send_message(channel, bot.translate("temp_str1").format(temp=temp) + " " + bot.translate("temp_str2").format(temp=temp_outdoor))
      else:
          bot.send_message(channel, bot.translate("temp_str3").format(temp=temp_outdoor))
