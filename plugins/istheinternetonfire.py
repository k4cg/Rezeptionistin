from plugin import Plugin
import re

class istheinternetonfire(Plugin):

    def help_text(self, bot):
        return bot.translate("security_help")

    def on_msg(self, bot, user_nick, host, channel, message):
        url = "https://istheinternetonfire.com/status.txt"
        msg = bot.sanitize(bot.getpage(url))
        msg = re.sub('<[^<]+?>', '', msg)
        #msg = re.sub('https?://[^\s]+', '', msg)
        if self.is_message_new(msg):
            self.save_message(msg)
            bot.send_message(channel, bot.translate("security_str1").format(msg=msg), user_nick)
        if message.startswith("!security"):
            bot.send_message(channel, bot.translate("security_str1").format(msg=msg), user_nick)

    def save_message(self, msg):
        f = open('/tmp/.internetbrenntcache','w')
        f.write(msg)
        f.close()

    def is_message_new(self, msg):
        try:
            f = open('/tmp/.internetbrenntcache')
            c = f.read()
        except IOError:
            c = "THISWILLNEVERHAPPEN"

        if c != msg:
            return True
        else:
            return False

