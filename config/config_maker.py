# -*- coding: utf-8 -*-
import ConfigParser
from PyQt4.QtCore import *

config = ConfigParser.RawConfigParser()
language = {
    'echo': "Qt.cyan",
    'print': "Qt.cyan",
    'while': "Qt.darkBlue",
    'for': "Qt.darkBlue",
    'try': "Qt.darkBlue",
    'catch': "Qt.darkBlue",
    'else': "Qt.darkBlue",
    'elseif': "Qt.darkBlue",
    'else': "Qt.darkBlue",
    'super': "Qt.darkBlue",
    'function': "Qt.darkBlue",
    'var': "Qt.darkBlue",
    'public': "Qt.darkBlue",
    'class': "Qt.darkBlue",
    'extends': "Qt.cyan",
    'implement': "Qt.cyan",
    'class': "Qt.darkBlue",
    'private': "Qt.darkBlue",
    'protected': "Qt.darkBlue",
    'switch': "Qt.darkBlue",
    'endswitch': "Qt.darkBlue",
    'throw': "Qt.darkBlue",
    'new': "Qt.darkBlue",
    'array': "Qt.cyan",
    'null': "Qt.cyan",

    }
# When adding sections or items, add them in the reverse order of
# how you want them to be displayed in the actual file.
# In addition, please note that using RawConfigParser's and the raw
# mode of ConfigParser's respective set functions, you can assign
# non-string values to keys internally, but will receive an error
# when attempting to write to a file or when you get it in non-raw
# mode. SafeConfigParser does not allow such assignments to take place.
config.add_section('Settings')
config.set('Settings', 'extension', 'php')
config.add_section('Language')
config.set('Language', 'language', language)

# Writing our configuration file to 'example.cfg'
with open('phpBrush.ini.', 'wb') as configfile:
    config.write(configfile)
