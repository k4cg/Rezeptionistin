import random
from plugin import Plugin

class Insult(Plugin):
  def help_text(self, bot):
    return bot.translate("insult_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith(bot.translate("insult_cmd")):
      if len(message.split()) >= 2:
      	if bot.getlanguage() == "de":
          bot.send_message(channel, message.split()[1] + ", du " + random.choice(list(open('lists/insults.txt'))), user_nick)
        elif bot.getlanguage() == "en":
          # source http://www.jokes4us.com/yomamajokes/yomamasofatjokes.html
          bot.send_message(channel, message.split()[1] + ", " + random.choice(list(open('lists/yomomma.txt'))), user_nick) 
