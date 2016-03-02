import random
from plugin import Plugin

class Flatter(Plugin):
  def help_text(self, bot):
    return bot.translate("flatter_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith(bot.translate("flatter_cmd")):
      if len(message.split()) >= 2:
        bot.send_message(channel, message.split()[1] + ", " + random.choice(list(open('lists/flattery.txt'))))

