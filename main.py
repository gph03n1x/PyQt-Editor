#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui
import core.brush.brush as brush


class Notepad(QtGui.QMainWindow):

    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()

    def initUI(self):
        newAction = QtGui.QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create new file')
        newAction.triggered.connect(self.newFile)

        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current file')
        saveAction.triggered.connect(self.saveFile)

        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.openFile)

        closeAction = QtGui.QAction('Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close Notepad')
        closeAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(closeAction)

        self.tab_widget = QtGui.QTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.setGeometry(300, 300, 900, 900)
        self.setWindowTitle('Notepad')
        self.show()

    def newFile(self):
        text_widget = QtGui.QTextEdit(self.tab_widget)
        text_widget.setFont(QtGui.QFont("Courier", 10))
        self.tab_widget.addTab(text_widget, "new")

    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File',
             os.path.join(os.path.expanduser('~'), 'Desktop'))
        f = open(filename, 'w')
        filedata = self.tab_widget.currentWidget().toPlainText()
        f.write(filedata)
        f.close()

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',
             os.path.join(os.path.expanduser('~'), 'Desktop'))
        f = open(filename, 'r')
        filedata = f.read()
        f.close()
        extension = filename.split(".")[-1]
        text_widget = QtGui.QTextEdit(self.tab_widget)
        text_widget.setFont(QtGui.QFont("Courier", 10))
        text_widget.setText(filedata)
        self.tab_widget.addTab(text_widget, os.path.basename(str(filename)))
        brush.highlightSyntax(text_widget).change_extension(extension)


def main():
    app = QtGui.QApplication(sys.argv)
    notepad = Notepad()
    notepad.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
