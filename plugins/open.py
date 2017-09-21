import re
import json
import ConfigParser
from plugin import Plugin

class Open(Plugin):

  def __init__(self, config=None):
    super(Open, self).__init__()

  def help_text(self, bot):
    return bot.translate("open_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.startswith("!offen") or message.startswith("!open"):
        msg = bot.get_spacestatus_data()
        wifi = msg['online']
        door = str(msg['hservierer']['door'])

        if int(wifi) > 0 and door == 'open':
          bot.send_message(channel, bot.translate("open_str1").format(d=wifi,door=door), user_nick)
        elif int(wifi) > 0 and door == 'closed':
          bot.send_message(channel, bot.translate("open_str2").format(d=wifi,door=door), user_nick)
        elif int(wifi) == 0 and door == 'open':
          bot.send_message(channel, bot.translate("open_str2").format(d=wifi,door=door), user_nick)
        else:
          bot.send_message(channel, bot.translate("open_str3").format(d=wifi,door=door), user_nick)
