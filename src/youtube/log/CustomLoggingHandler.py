'''Testing License v0.1'''
'''
Created on Oct 31, 2010
Taken from: http://old.nabble.com/logging.Handler-not-working-with-QThreads-td22214831.html
@author: Rahul
'''
import logging 
from PyQt4.QtCore import QMutex
from PyQt4.QtGui import QTextCursor, QColor
class QtStreamHandler(logging.Handler): 
    def __init__(self, parent, main): 
        logging.Handler.__init__(self) 
        self.parent = parent 
        self.main = main         
        self.textWidget = parent 
        self.formater = logging.Formatter("%(asctime)s - %(levelname)s -> %(message)s") 
        self.logString = ""
    def getLoggingCompleteText(self):
        return self.logString
    def createLock(self): 
        self.mutex = QMutex() 
    
    def acquire(self): 
        self.mutex.lock() 
    
    def release(self): 
        self.mutex.unlock() 
    
    def emit(self, record): 
#        self.textWidget.appendPlainText(self.formater.format(record))
        formattedText = self.formater.format(record)
        #separate text from date
        index = formattedText.find('->')
        self.textWidget.setTextColor(QColor("green"))
        self.textWidget.insertPlainText(formattedText[:index])
        self.textWidget.setTextColor(QColor("blue"))
        self.textWidget.insertPlainText(formattedText[index:] + "\n") 
        self.textWidget.moveCursor(QTextCursor.EndOfLine) 
        self.textWidget.ensureCursorVisible() 
        self.logString += formattedText + "\n";
