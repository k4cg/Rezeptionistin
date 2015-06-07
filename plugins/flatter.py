import random
from plugin import Plugin

class Flatter(Plugin):
  def help_text(self):
    return "!schmeichle <nick> - Jemandem ein Kompliment machen."

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!schmeichle'):
      if len(message.split()) >= 2:
        bot.send_message(channel, message.split()[1] + ", " + random.choice(list(open('lists/flattery.txt'))))

