from plugin import Plugin

class Urls(Plugin):
  def help_text(self, bot):
    return (bot.translate("url_help"+"\n") + bot.translate("url_help2"))

  def on_msg(self, bot, user_nick, host, channel, message):
    if bot.httpregex.search(message.lower()) is not None:
      url = bot.geturlfrommsg(message)
      title = bot.sanitize(bot.geturltitle(url))
      if not title == "":
        if message.lower().startswith('!private') or message.lower().startswith('!pr'):
          bot.send_message(channel, "[private] " + "Title: {title}".format(title=title))
        elif message.lower().startswith('!nsfw'):
          bot.send_message(channel, "[nsfw] " + "Title: {title}".format(title=title))
        else:
          bot.send_message(channel, "Title: {title}".format(title=title))
          print bot.get_plugin("MediaWiki").wikiupdate(title, url)
