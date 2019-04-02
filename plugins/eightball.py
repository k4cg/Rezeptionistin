import random
from plugin import Plugin

class Eightball(Plugin):
  def help_text(self, bot):
    return bot.translate("eightball_help")

  def answer(self, bot, msg, recipient, nick=None):
    keywords = ["kann ich", "was kann ich", "wie kann ich", "darf ich", "was darf ich", "soll ich", "was soll ich", "wie soll ich", "muss ich", "was muss ich"]
    if any(msg.lower().startswith(k) for k in keywords):
      adressee = (nick + ": ") if nick else ""

      if "oder" in msg:
        bot.send_message(recipient, adressee + random.choice(list(open('lists/alternate_answers.txt'))), nick)
      else:
        bot.send_message(recipient, adressee + random.choice(list(open('lists/polar_answers.txt'))), nick)

  def on_msg(self, bot, user_nick, host, channel, message):
    self.answer(bot, message, channel, user_nick)

  def on_privmsg(self, bot, user_nick, host, message):
    self.answer(bot, message, user_nick)
