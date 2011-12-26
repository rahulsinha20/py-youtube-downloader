''' Copyright (C) 2010 Abhijat Sinha (Rahul)    
    "This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."
     
    '''
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
