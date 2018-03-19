# coding: utf8

from plugin import Plugin

class Status(Plugin):

  def __init__(self, config=None):
    super(Status, self).__init__()

  def help_text(self, bot):
    return bot.translate("status_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.startswith("!status") or message.startswith("!st"):
        msg = bot.get_spacestatus_data()

        if msg is None:
          bot.send_message(channel, bot.translate("status_error"), user_nick)
        else:
          noise = str(msg['sound'])
          temp = str(msg['temp'])
          light = str(msg['light'])
          hosts = str(msg['online'])
          door = str(msg['door'])

          bot.send_message(channel, bot.translate("status_str1").format(noise=noise, temp=temp, light=light, hosts=hosts, door=door), user_nick)
