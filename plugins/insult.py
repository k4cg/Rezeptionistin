import random
from plugin import Plugin

class Insult(Plugin):
  def help_text(self):
    return "!beleidige <nick> - Jemanden beleidigen."

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!beleidige'):
      if len(message.split()) >= 2:
        bot.send_message(channel, message.split()[1] + ", du " + random.choice(list(open('lists/insults.txt'))))
