from plugin import Plugin
import re
import json

class openstatus(Plugin):

    def help_text(self):
        return ("!offen - Aktuelle Geraete in der K4CG anzeigen lassen")

    def on_privmsg(self, bot, user_nick, host, channel, message):
        if message.startswith("!offen"):
          msg = bot.sanitize(bot.getopenstatus())
          msg = json.loads(msg)
          f = msg['online']

          if int(f) > 0:
            bot.send_message(channel, "Wahrscheinlich. Momentan sind {d} Geraete in der K4CG".format(d=f))
          else:
            bot.send_message(channel, "Sorry, sieht nicht so aus als waere jemand in der K4CG".format(d=f))

