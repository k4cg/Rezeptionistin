from plugin import Plugin

class Playlist(Plugin):

  def help_text(self, bot):
    return bot.translate("playlist_help")

  def on_msg(self, bot, user_nick, host, channel, message):
    if message.lower().startswith('!np'):
      bot.send_message(channel, "Das funktioniert noch nicht.")
