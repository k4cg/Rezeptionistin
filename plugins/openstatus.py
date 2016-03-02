import re
import json
import ConfigParser
from plugin import Plugin

class OpenStatus(Plugin):

  def __init__(self, config=None):
    try:
      self.openstatus = config.get('OpenStatus', 'url')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
      print "OpenStatus was not properly configured in your config.ini"
    super(OpenStatus, self).__init__()

  def help_text(self, bot):
    return bot.translate("openstatus_help")

  def on_privmsg(self, bot, user_nick, host, channel, message):
    if message.startswith("!offen") or message.startswith("!open"):
      if hasattr(self, "openstatus"):
        msg = bot.sanitize(self.get_status())
        msg = json.loads(msg)
        f = msg['online']

        if int(f) > 0:
          bot.send_message(channel, "Wahrscheinlich. Momentan sind {d} Geraete in der K4CG".format(d=f))
        else:
          bot.send_message(channel, "Sorry, sieht nicht so aus als waere jemand in der K4CG".format(d=f))
      else:
        print "OpenStatus Error: [OpenStatus] url is not configured in your config.ini"

  def get_status(self):
    j = self.getpage(self.openstatus)
    return j
