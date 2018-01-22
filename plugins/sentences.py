from plugin import Plugin
import random
import markovify

class Sentences(Plugin):

  def __init__(self, config=None):
    try:
      self.satzgenerator = config.get('Sentences', 'satzgenerator')
      self.markov = config.get('Sentences', 'markov')
      self.markovfile = config.get('Sentences', 'markovfile')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
      print "Sentences was not properly configured in your config.ini"

    try:
      with open(self.markovfile) as f:
          text = f.read()
      self.markov_model = markovify.Text(text)
    except IOError:
      print "Problems opening your markov file %s" % self.markovfile
    super(Sentences, self).__init__()

  def get_markov_sentence(self):
    l = random.randint(80,120)
    return self.markov_model.make_short_sentence(l)

  def on_msg(self, bot, user_nick, host, channel, message):
    if bot.nick.lower() in message.lower():
      if self.satzgenerator == 'off':
        sentence = self.get_markov_sentence()
      elif self.markov == 'off':
        sentence = bot.geturltitle("https://www.satzgenerator.de/neu").replace("Satzgenerator: ", "")
      else:
        if random.random() >= 0.5:
          sentence = bot.geturltitle("https://www.satzgenerator.de/neu").replace("Satzgenerator: ", "")
        else:
          sentence = self.get_markov_sentence()

      bot.send_message(channel, bot.sanitize(sentence), user_nick)
