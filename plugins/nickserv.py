from plugin import Plugin

class Nickserv(Plugin):

  def help_text(self):
    return "Mich beim freenode NickServ authentifizieren."

  def on_join(self, bot, user_nick, host, channel):
    if bot.ircchan == "#" + channel:
        bot.send_command("NickServ", "identify " + bot.nickservpassword)
