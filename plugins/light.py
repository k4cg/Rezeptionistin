from plugin import Plugin

class Light(Plugin):

  def __init__(self, config=None):
    super(Light, self).__init__()

  def help_text(self, bot):
    return bot.translate("light_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.startswith("!licht") or message.startswith("!light"):
        msg = bot.get_spacestatus_data()
        f = msg['light']

        if float(f) > 0:
          bot.send_message(channel, bot.translate("Light_str1").format(light=f), user_nick)
        else:
          bot.send_message(channel, bot.translate("Light_str2").format(light=f), user_nick)

