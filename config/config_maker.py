# -*- coding: utf-8 -*-
LANGUAGE = "php"
EXTENSION = "php"
LANGUAGE_SYNTAX = {
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

import ConfigParser
# Create a quick brush.ini
config = ConfigParser.RawConfigParser()
# Set extension and language syntax
config.add_section('Settings')
config.set('Settings', 'extension', EXTENSION)
config.add_section('Language')
config.set('Language', 'language', LANGUAGE_SYNTAX)
# write them in the brush.ini file
with open(LANGUAGE+'Brush.ini.', 'wb') as configfile:
    config.write(configfile)
