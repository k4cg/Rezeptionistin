# coding: utf8

import socket
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_sound_intensity import BrickletSoundIntensity
from plugin import Plugin

class Sound(Plugin):

  def __init__(self, config=None):
    try:
      self.sound_host = config.get('Geraeusche', 'host')
      self.sound_port = config.get('Geraeusche', 'port')
      self.sound_id = config.get('Geraeusche', 'id')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
      print "Geraeusche was not properly configured in your config.ini"
    super(Sound, self).__init__()

  def help_text(self, bot):
    return bot.translate("sound_help")

  def get_sound(self):
    ipcon = IPConnection()
    uvl = BrickletSoundIntensity(self.sound_id, ipcon)
    ipcon.connect(self.sound_host, int(self.sound_port))
    intensity = uvl.get_intensity()
    ipcon.disconnect()
    return(str(intensity))

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!geraeusche') or message.lower().startswith('!sound'):
      m = self.get_sound()
      if not m == '':
        bot.send_message(channel, 'Momentane Geraeuschintensitaet: ' + m + '/3300')
      else:
        bot.send_message(channel, 'Geraeuschintensitaet konnte *nicht* abgefragt werden')
