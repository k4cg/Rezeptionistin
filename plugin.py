# Plugin Base Class

class Plugin(object):

  def __init__(self):
    pass

  # meta
  #

  def help_text(self):
    return ""

  # irc event handlers
  #

  def on_msg(self, bot, user_nick, host, channel, message):
    pass

  def on_privmsg(self, bot, user_nick, host, message):
    pass
