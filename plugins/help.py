from plugin import Plugin

class Help(Plugin):
  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!help'):
      bot.send_message(user_nick, bot.translate("help_hello"))
      bot.send_message(user_nick, bot.translate("help_intro"))
      for plugin in bot.plugins:
        text = plugin.help_text()
        if text != "":
          for t in text.split("\n"):
            bot.send_message(user_nick, t)

