from plugin import Plugin

class Alive(Plugin):
  def help_text(self, bot):
    return bot.translate("alive_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!gt'):
      bot.send_message(channel, bot.translate("alive_str1").format(nick=user_nick))

  def on_privmsg(self, bot, user_nick, host, message):
    if message.lower().startswith('!gt'):
      bot.send_message(user_nick, bot.translate("alive_str1").format(nick=user_nick))

