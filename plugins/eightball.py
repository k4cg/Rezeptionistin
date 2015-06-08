import random
from plugin import Plugin

class Eightball(Plugin):
  def on_msg(self, bot, user_nick, host, channel, message):
    keywords = ["kann ich", "darf ich", "soll ich", "muss ich"]
    if any(message.lower().startswith(k) for k in keywords):
      if "oder" in message:
        bot.send_message(channel, user_nick + ": " + random.choice(list(open('lists/alternate_answers.txt'))))
      else:
        bot.send_message(channel, user_nick + ": " + random.choice(list(open('lists/polar_answers.txt'))))
