# coding: utf8

from plugin import Plugin

class Sound(Plugin):

  def __init__(self, config=None):
    super(Sound, self).__init__()

  def help_text(self, bot):
    return bot.translate("sound_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.startswith("!noise") or message.startswith("!geraeusche"):
        msg = bot.get_spacestatus_data()
        f = str(msg['sound'])

        if float(f) > 0:
          bot.send_message(channel, bot.translate("Sound_str1").format(sound=f), user_nick)
        else:
          bot.send_message(channel, bot.translate("Sound_str2").format(sound=f), user_nick)
