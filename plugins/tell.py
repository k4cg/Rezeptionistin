import json
import random
from datetime import datetime
from plugin import Plugin

class Tell(Plugin):

  messages = []

  def __init__(self):
    try:
      with open('tell_messages.json') as infile:
        self.messages = json.load(infile)
    except IOError:
      pass
    super(Tell, self).__init__()


  def help_text(self):
    return "!sage <nick> <nachricht> - Einem Benutzer eine Nachricht ausrichten wenn er das naechste mal auftaucht."

  def tell(self, bot, user_nick, receiver, message):
    reply_to = user_nick if receiver == bot.nick else receiver

    if message.lower().startswith('!sage'):
      if (len(message.rstrip().split()) < 3) or (len(bot.split_by_nth(message.rstrip(), 2)[1]) <= 0):
        bot.send_message(reply_to, user_nick + ": Benutzung: !sage <nick> <nachricht>")
      elif len(bot.split_by_nth(message, 2)[1]) > 144:
        bot.send_message(reply_to, user_nick + ": Bitte bleibe unter 144 Zeichen.")
      else:
        recipient = message.split()[1]
        message = message.split(recipient)[1].strip()
        senttime = datetime.now().strftime('%d.%m.%Y %H:%M')

        new_message = {
          "date": senttime.split()[0],
          "time": senttime.split()[1],
          "sender": user_nick,
          "recipient": recipient,
          "message": message,
          "send_to": recipient if receiver == bot.nick else receiver
        }

        self.messages.append(new_message)

        with open('tell_messages.json', 'w+') as outfile:
          json.dump(self.messages, outfile)

        bot.send_message(reply_to, "Alles klar, mach ich.")

  def on_join(self, bot, user_nick, host, channel):
    user_messages = [message for message in self.messages if message["recipient"] == user_nick]
    for message in user_messages:
      if (not message["send_to"].startswith("#")) or (message["send_to"][1:] == channel):
        bot.send_message(message["send_to"], user_nick + ", " + message["sender"] + " liess dir am " + message["date"] + " um " + message["time"] + " Uhr ausrichten: " + message["message"])
        self.messages.remove(message)

    with open('tell_messages.json', 'w+') as outfile:
      json.dump(self.messages, outfile)

  def on_msg(self, bot, user_nick, host, channel, message):
    self.tell(bot, user_nick, channel, message)
