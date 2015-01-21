# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ConfigParser
import os
import ast
global dict_mod


try:
    modnames = [name for name in os.listdir("config")
     if name.endswith("Brush.ini")]
    dict_mod = {}
    for lib in modnames:
        config = ConfigParser.ConfigParser()
        config.read('config/' + lib)
        _ext_ = config.get('Settings', 'extension', 0)
        dict_mod[QString(_ext_)] = ast.literal_eval(config.get('Language',
         'language', 0))

except Exception:
    pass


class highlightSyntax(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(highlightSyntax, self).__init__(parent)
        self.highlightingRules = []
        self.basic_regexes()

    def hl_k(self, color):
        brush = QBrush(eval(color), Qt.SolidPattern)
        keyword = QTextCharFormat()
        keyword.setForeground(brush)
        keyword.setFontWeight(QFont.Bold)
        return keyword

    def basic_regexes(self):
        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append(hl_r(QRegExp("#[^\n]*"),
                singleLineCommentFormat))
        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append(hl_r(QRegExp("\".*\""),
                quotationFormat))
        self.highlightingRules.append(hl_r(QRegExp("\'.*\'"),
                quotationFormat))
        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        functionregex = QRegExp("\\b[A-Za-z0-9_]+(?=\\()")
        self.highlightingRules.append(hl_r(functionregex,
                functionFormat))

    def change_extension(self, extension):
        self.highlightingRules = []
        try:
            self.highlightingRules = [hl_r(QRegExp("\\b" + word + "\\b"),
                self.hl_k(dict_mod[extension][word]))
                for word in dict_mod[extension]]
        except KeyError:
            pass
        self.basic_regexes()

    def highlightBlock(self, text):
        for rule in self.highlightingRules:
            expression = QRegExp(rule.pattern)
            index = expression.indexIn(text)

            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, rule.format)
                index = text.indexOf(expression, index + length)

        self.setCurrentBlockState(0)


class hl_r(object):
    def __init__(self, pattern, format):
        self.pattern = pattern
        self.format = format
