from plugin import Plugin

class Urls(Plugin):

def help_text(self, bot):
    return (bot.translate("url_help") + "\n" + bot.translate("url_help2"))

def on_msg(self, bot, user_nick, host, channel, message):
    ms = message.lower()

    if bot.httpregex.search(ms) is None:
        return False

    # extract list of arrays from message
    urls = bot.geturlsfrommsg(message)

    # loop through all items
    for url in urls:

        # fetch html <title> element
        title = bot.sanitize(bot.geturltitle(url))

        # Check if link can be added to wiki
        if not ms.startswith('!private') and not ms.startswith('!pr') and not ms.startswith('!nsfw'):

            # Set proper wikititle
            if title == "":
                title = url

            # call bot and paste to wiki
            bot.get_plugin("MediaWiki").wikiupdate(wikititle, url)

        # If empty title, dont paste to irc
        if title == "":
            continue

        # check if private link
        if ms.startswith('!private') or ms.startswith('!pr'):
            bot.send_message(channel, "[private] " + "Title: {title}".format(title=title), user_nick)

        # check if link was marked as nsfw from sender
        elif ms.startswith('!nsfw'):
            bot.send_message(channel, "[nsfw] " + "Title: {title}".format(title=title), user_nick)

        # send title to
        else:
            bot.send_message(channel, "Title: {title}".format(title=title), user_nick)



