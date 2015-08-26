import random
from plugin import Plugin

class Insult(Plugin):
  def help_text(self):
    return "!lineart - Zeige eine lineart"

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!lineart'):
      if len(message.split()) >= 1:
        bot.send_message(channel, random.choice(list(open('lists/lineart.txt'))))
