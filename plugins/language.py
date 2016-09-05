from plugin import Plugin

class Language(Plugin):
  def help_text(self, bot):
    return bot.translate("language_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!lang'):
     if len(message.split()) >= 2:
      if bot.setlanguage(message.split()[1]) == True:
      	bot.send_message(channel, bot.translate("language_str1"), user_nick)
      else:
      	bot.send_message(channel, bot.translate("language_str2"), user_nick)
