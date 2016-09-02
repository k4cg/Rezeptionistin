# coding: utf8

import socket
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_uv_light import BrickletUVLight
from plugin import Plugin

class Licht(Plugin):

  def __init__(self, config=None):
    try:
      self.licht_host = config.get('Licht', 'host')
      self.licht_port = config.get('Licht', 'port')
      self.licht_id = config.get('Licht', 'id')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
      print "Licht was not properly configured in your config.ini"
    super(Licht, self).__init__()

  def help_text(self, bot):
    return bot.translate("licht_help")

  def get_light(self):
    ipcon = IPConnection()
    uvl = BrickletUVLight(self.licht_id, ipcon)
    ipcon.connect(self.licht_host, int(self.licht_port))
    uv_light = uvl.get_uv_light()
    ipcon.disconnect()
    return(str(uv_light) + " µW/cm²")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!licht'):
      m = self.get_light()
      bot.send_message(channel, 'Momentane Lichtverhaeltnisse: ' + m)
