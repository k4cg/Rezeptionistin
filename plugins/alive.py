from plugin import Plugin

class Alive(Plugin):
  def help_text(self):
    return "!gt - Guten Tag wuenschen."

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!gt'):
      bot.send_message(channel, "Ich lebe noch, {nick}".format(nick=user_nick))

  def on_privmsg(self, bot, user_nick, host, message):
    if message.lower().startswith('!gt'):
      bot.send_message(user_nick, "Ich lebe noch, {nick}".format(nick=user_nick))

