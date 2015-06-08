#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import logging
from rezeptionistin import Rezeptionistin

reload(sys)
sys.setdefaultencoding("utf-8")

# start logging
logging.basicConfig(level=logging.DEBUG)

if sys.hexversion > 0x03000000:
  raw_input = input

# run bot
bot = Rezeptionistin()
bot.run()
