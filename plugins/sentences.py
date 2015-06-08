from plugin import Plugin

class Sentences(Plugin):
  def on_msg(self, bot, user_nick, host, channel, message):
    if bot.nick.lower() in message.lower():
      sentence = bot.geturltitle("https://www.satzgenerator.de/neu").replace("Satzgenerator: ", "")
      bot.send_message(channel, bot.sanitize(sentence))
