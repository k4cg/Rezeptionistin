import socket
from plugin import Plugin

class Temperature(Plugin):
  def help_text(self):
    return "!kt - Zeige aktuelle Temperatur in der K4CG."

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!kt'):
      temp = bot.netcat("2001:a60:f073:0:21a:92ff:fe50:bdfc", 31337, "9001")
      bot.send_message(channel, "Die aktuelle Temperatur in der K4CG ist{temp} Grad".format(temp=temp) )
