import random
from plugin import Plugin

class Insult(Plugin):
  def help_text(self, bot):
    return bot.translate("lineart_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!lineart'):
      if len(message.split()) >= 1:
        bot.send_message(channel, random.choice(list(open('lists/lineart.txt'))), user_nick)

  def on_privmsg(self, bot, user_nick, host, message):
    if message.lower().startswith('!lineart'):
      if len(message.split()) >= 1:
        bot.send_message(user_nick, random.choice(list(open('lists/lineart.txt'))), user_nick)
