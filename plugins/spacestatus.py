import re
import json
import ConfigParser
from plugin import Plugin

class Open(Plugin):

  def __init__(self, config=None):
    super(Open, self).__init__()

  def help_text(self, bot):
    return bot.translate("spacestatus_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.startswith("!offen") or message.startswith("!open"):
        msg = bot.get_spacestatus_data()
        f = msg['online']

        if int(f) > 0:
          bot.send_message(channel, bot.translate("spacestatus_str1").format(d=f), user_nick)
        else:
          bot.send_message(channel, bot.translate("spacestatus_str2").format(d=f), user_nick)
