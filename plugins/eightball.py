import random
from plugin import Plugin

class Eightball(Plugin):
  def help_text(self):
    return "fragen beantworten in Form: <soll/kann/darf/muss> ich * [<oder> *]"
  
  def answer(self, bot, msg, recipient, nick=None):
    keywords = ["kann ich", "darf ich", "soll ich", "muss ich"]
    if any(msg.lower().startswith(k) for k in keywords):
      adressee = (nick + ": ") if nick else ""

      if "oder" in msg:
        bot.send_message(recipient, adressee + random.choice(list(open('lists/alternate_answers.txt'))))
      else:
        bot.send_message(recipient, adressee + random.choice(list(open('lists/polar_answers.txt'))))    
  
  def on_msg(self, bot, user_nick, host, channel, message):
    self.answer(bot, message, channel, user_nick)

  def on_privmsg(self, bot, user_nick, host, message):
    self.answer(bot, message, user_nick)
