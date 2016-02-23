import ConfigParser
from wikitools import wiki
from wikitools import category
from plugin import Plugin

class MediaWiki(Plugin):
  def __init__(self, config=None):
    if config:
      try:
        self.site = wiki.Wiki(config.get('MediaWiki', 'wikiapiurl'))
        self.site.login(config.get('MediaWiki', 'user'), config.get('MediaWiki', 'password'))

      except ConfigParser.NoSectionError:
        print "MediaWiki Error: Please configure the [MediaWiki] section in your config.ini"
      except ConfigParser.NoOptionError:
        print "MediaWiki Error: Mediawiki Url or login credentials are not configured in your config.ini"

    super(MediaWiki, self).__init__()

  def wikiupdate(self, title, url):
    cat = category.Category(self.site, "Linklist")
    for article in cat.getAllMembersGen(namespaces=[0]):
      print article.edit(appendtext="\n* {title} - {url} \n".format(title=title, url=url))
