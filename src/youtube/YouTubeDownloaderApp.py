'''
Created on Jun 30, 2009
This is the main UI Launcher class which displays the UI and also acts as the controller
It has slots for various events passed from the UI
@author: Rahul Sinha
'''
import sys
import logging
import webbrowser
import os
from PyQt4.QtGui import QSplashScreen, QImage, QPixmap, QProgressBar
import youtube.util.downloader.GenericDownloader
import youtube.gui.components.LibraryFileWidgetItem
import youtube.util.xml.PropertiesAccessor
from youtube.log.CustomLoggingHandler import QtStreamHandler
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QString
from youtube.gui.core.YouTubeDownloaderMainWindow import Ui_MainWindow
from youtube.util.VlcPlayer import VlcPlayer
from youtube.util.videoservice.VideoSearch import VideoSearch
from youtube.gui.util.CustomizedDirectDownloadButton import CustomizedDirectDownloadButton
class StartMainWidget(QtGui.QMainWindow):
    ''' This class is the controller for the Widget view'''
    def __init__(self, parent=None):
        ''' Is the non default constructor that sets up the main widget'''
        QtGui.QMainWindow.__init__(self, parent)
        #Invoke the splash screen     
        self.SplashScreenInitator()          
        #Read application configuration
        self.properties = youtube.util.xml.PropertiesAccessor.PropertiesAccessor()
        #Store the return status from configuration
        returnCode = self.properties.readProperties()
        #set library path and vlc path        
        self.libraryPath = self.properties.getLibraryPath()
        self.vlcPath = self.properties.getVlcPath()
        #Variables
        self.totalVideosQueuedForDownload = 0
        #Setup the Main Window
        self.ui = Ui_MainWindow()
        #Draw its components
        self.ui.setupUi(self)
        #Setup logger
        self.log = logging.getLogger("Logger")
        #Set log level
        self.log.setLevel(logging.INFO)
        #Set up a handler - we direct all the log messages to the text edit component
        self.loggingHandler = QtStreamHandler(self.ui.textEdit, self)
        #Add the text edit handler
        self.log.addHandler(self.loggingHandler)
        self.log.info("YouTube Downloader version 2.0 Started...")
        #Check if there was a valid configuration file found
        if returnCode == -1:
            #No Configuration file found
            self.showSettingsDialogSlot()
        else:
            #Upload video library listing
            self.updateVideoLibrary()
        self.videoList = {}
        #Signal for double clicking (playback) a video track from library
        QtCore.QObject.connect(self.ui.treeWidget, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"), self.playVideo)
        #Bind an action for menu selection on Settings
        QtCore.QObject.connect(self.ui.actionSettings, QtCore.SIGNAL("triggered()"), self.showSettingsDialogSlot)
        #Bind an action for menu selection on Author
        QtCore.QObject.connect(self.ui.actionVideo_Downloader, QtCore.SIGNAL("triggered()"), self.showAboutDialogSlot)
        #BInd an action for video search
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.beginButtonSlot)
        #Combo Box slot for Standard feeds
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("activated(int)"), self.comboBoxSlot)
#        #Slot for indicating that web kit has loaded the page/media
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("loadFinished(bool)"), self.mediaLoaded);
        #install an event filter on the tree widget to detect DEL key
        self.ui.treeWidget.installEventFilter(self)
        self.statusBar().showMessage("Application Started", 2000)
        
    def SplashScreenInitator(self):
        '''
        This initiates the splash screen and posts messages
        '''
        splash.showMessage("     Loading Modules ....")
        for counter in range(1, 200000):
            print ''
            #find percentage of what is loaded
            progressBar.setValue(int(counter / float(200000) * 100))
            if counter == 50000:
                splash.showMessage("     Core Framework Started ...")
               
            if counter == 100000:
                splash.showMessage("     Interface Initialized ...")
                
            if counter == 150000:
                splash.showMessage("     Media Library Loading ...")
#                for counter2 in range (1, 1000000):
#                    print ''
                splash.showMessage("     Media Library Loaded ...")
                
    def closeEvent(self, e):
        '''
        Overriden slot for window close event - this is invoked when user closes
        the window from X
        '''
        self.flushBeforeExit()
                 
    def eventFilter(self, obj, ev):
        '''
        Event Filter allows keys events to be detected for the UI Controller
        '''
        if (ev.type() == QtCore.QEvent.KeyPress):
            #Check if this is a valid object 
            if (obj.currentItem() == None):
                return False
            #Check if the key is F5 for Refresh
            if ev.key() == QtCore.Qt.Key_F5:               
                #check if we are at the root node
                if (obj.currentItem().text(0) == 'Video Library'):
                    self.updateVideoLibrary()
                    return True
            #Check if the pressed key is a DEL
            if ev.key() == QtCore.Qt.Key_Delete:
                #Check if this key is not at the root
                if (obj.currentItem().text(0) == 'Video Library'):
                    return False
                #Also check if we are currently not playing this video
                if obj.currentItem().getQueuedStatus() == True:
                    self.log.info("Selected file for deletion is currently queued")
                    self.log.info("Try Refreshing the video library by selecting the root node and pressing F5")                   
                self.log.info('Del Key Press Detected for Item:' + obj.currentItem().text(0))                
                self.tokenList = []                
                #Now we need to recursively traverse till we reach the root        
                #get the current widget item
                self.__recursiveSearch__(obj.currentItem())
                #Now from the token list reading backwards form the complete path
                pathToDelete = self.libraryPath
                for tokenText in reversed(self.tokenList):
                    pathToDelete += "/" + tokenText
                print pathToDelete 
                #QString to string
                path = str(pathToDelete)
                path = path.replace("\\", "/")
                #check if the path to delete is a folder or a file
                if os.path.isdir(path) == True:
                    #We are deleting a folder
                    self.log.info('Full Path For Folder Deletion:' + path)    
                    try:
                        os.rmdir(path)
                        #re-load video library
                        self.updateVideoLibrary()
                    except OSError:
                        self.log.fatal('Path is not empty!')
                else:
                    #This is a file
                    self.log.info('Full Path For File Deletion:' + path) 
                    try:   
                        os.remove(path)
                        #re-load video library
                        self.updateVideoLibrary()
                    except WindowsError:
                        self.log.fatal("The process cannot access the file because it is being used by another process:")               
                return True #indicating the event was consumed                
        return False #Let other filters process this event
    
    def mediaLoaded(self, state):
        '''
        Slot indicating that media is loaded
        '''
        self.log.info("Media Loaded")
        if state == True:
            QtGui.QApplication.setOverrideCursor(QtCore.Qt.ArrowCursor);
            
    def comboBoxSlot(self, index):
        '''
        This is the slot for combo box
        '''
        if index != 0:
            #User has selected a standard feed
            #Disable search edit text
            self.ui.lineEdit.setDisabled(True)
        else:
            self.ui.lineEdit.setDisabled(False)
            
    def getLibraryPath(self):
        '''
        Returns library path - used by Downloader class to store videos in the
        current directory
        '''
        return self.libraryPath
    
    def showSettingsDialogSlot(self):
        '''
        This displays a dialog for App configurable settings
        '''
        self.ui.settingsDialog.setVisible(True)
        
    def showAboutDialogSlot(self):
        '''
        This displays a dialog for About App
        '''
        self.ui.aboutAuthorDialog.setVisible(True)
    
#    def doubleClickedSlot(self):
#        self.log.info('CLicked')
    
    def setVlcPath(self, newVlcPath):
        '''
        This changes current VLC Path
        '''
        self.vlcPath = newVlcPath
        
    def setLibraryPath(self, newPath):
        '''
        This mutator is called from the Settings Dialog to change the library path
        '''
        self.libraryPath = newPath
    
    def clearButtonSlot(self):
        '''Action Handler for clear button on the main window - It sets components to defaults'''
        (self.ui.progressBar).setValue(0)
        (self.ui.lineEdit).setText("")
        (self.ui.textEdit).clear()
        (self.ui.textEdit_2).clear()
        (self.ui.clearWidgetsFromLayout())
        self.ui.addDefaultPic()
        self.clearDownloadVideoStatus()
        self.totalVideosQueuedForDownload = 0
        self.clearVideoList()
        self.ui.label_4.setText('Not Selected')
        self.ui.label_6.setText('Not Applicable')
        self.ui.label_8.setText('Not Applicable')
        self.ui.label_10.setText('Not Applicable')
        #Also set combo box to its default state
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.lineEdit.setEnabled(True)
        self.ui.lineEdit.setText('')

    
    def clearDownloadVideoStatus(self):
        '''
        Clears video status which are queued for download
        '''
        self.ui.lineEdit_3.setText('')
        self.totalVideosQueuedForDownload = 0

    def clearVideoList(self):
        '''
        This clears current video list dictionary {title,link}
        '''
        self.videoList = {}
    def updateViewDownloadProgress(self, value):
        '''
        This is called from the downloader to update progress bar with a value
        '''
        self.ui.progressBar.setValue(value)
    def beginButtonSlot(self):        
        '''Slot to handle search action on the Main Window - It invokes UTube Web services
        using VideoSearch class'''
        self.ui.showSearchProgressBarOnView()   
        self.v = VideoSearch()
        #Check if we are searching for standard feeds
        if self.ui.comboBox.currentIndex() != 0:
            #Standard feed is selected, get its name
            self.v.begin('', True, str(self.ui.comboBox.currentText()))
        else:
            self.v.begin(str(self.ui.lineEdit.text()), False, None)
        QtCore.QObject.connect(self.v, QtCore.SIGNAL("finished()"), self.callbackSearchComplete)
        QtCore.QObject.connect(self.v, QtCore.SIGNAL("terminated()"), self.callbackSearchComplete)
        #Begin Thread
        self.v.start()

    def callbackSearchComplete(self):
        '''
        This method is called by the VideoSearch class once it finishes searching 
        for videos
        '''
        self.ui.progressBarSearch.close()
        self.log.info("Size of videos retrieved:" + str(len(self.v.videoList)))
        self.ui.receiveVideoListcallback(self.v.videoList)
    
    def endApp(self):
        self.log.info("App Closing")
    
    def changeLibraryPath(self):
        '''
        This is called from the view to change library path.
        This provides the same functionality as called from the settings dialog
        '''
        newPath = self.showBrowseDialog()
        if newPath != '':
            self.setLibraryPath(newPath)
            #Update video library
            self.updateVideoLibrary()    
            #Also update the config file
            properties = youtube.util.xml.PropertiesAccessor.PropertiesAccessor()
            properties.write(str(newPath), self.vlcPath)
    
    def showBrowseDialog(self):
        '''
        Shows Browse Dialog
        '''
        browseDialog = QtGui.QFileDialog(self, "Select Library Location")        
        browseDialog.setFileMode(QtGui.QFileDialog.Directory)
        browseDialog.setOption(QtGui.QFileDialog.ShowDirsOnly)       
        browseDialog.setViewMode(QtGui.QFileDialog.Detail)
        path = ''
        if (browseDialog.exec_()):
            folderNames = browseDialog.selectedFiles()
            #Get the first QString from QSTringList
            path = str(folderNames.takeAt(0))
            self.log.info('Library Location:' + path)
        return path
    def setEmbeddedVideosState(self, value):
        '''
        This sets whether embedded videos are enabled. If yes, videos are shown on the interface
        otherwise invokes the default browser
        '''
        self.ui.UpdateEmbeddedVideoState(value)
    
    def setMediaPlayerState(self, value):
        '''
        This sets flag to indicate whether media player is used to play library videos
        '''
        self.ui.UpdateMediaPlayerState(value)
        
    def updateVideoLibrary(self):
        '''
        This loads up all video files on the view
        '''
        #Check if there are any items already loaded - if yes, clear all 
        if (self.ui.treeWidget.topLevelItem(0) != None):
            self.ui.treeWidget.clear()
        #Update status for the library path on the main window
        self.ui.lineEdit_2.setText(self.libraryPath)
        self.ui.treeWidget.setColumnCount(1)
        rootItem = QtGui.QTreeWidgetItem(QtCore.QStringList("Video Library"))
        rootItem.setIcon(0, QtGui.QIcon('./resources/root.gif'))
        try:
            self.getFilesInDirectory(self.libraryPath, rootItem)
        except:
             self.showSettingsDialogSlot()
        self.ui.treeWidget.addTopLevelItem(rootItem)
        #Expand all nodes from the root
        self.ui.treeWidget.expandAll()
        self.ui.treeWidget.repaint()
    def __recursiveSearch__(self, widgetItem):
        #check if the parent is the root node
        
        if (widgetItem.text(0) == 'Video Library'):
            return - 1
        else:
            #self.recursivePath +=  widgetItem.text(0)+"/"
            self.tokenList.append(widgetItem.text(0))
            widgetItem = widgetItem.parent()
            ret = self.__recursiveSearch__(widgetItem)
            return ret
        
    def playVideo(self):
        '''
        This is the slot that plays the video by invoking an external vlc
        instance. It also checks if the video entry is already not queued.
        '''
        #Get Parent - check if we are not at the root node
        if (self.sender().currentItem().text(0) == 'Video Library'):
            return
        #Check if media player is enabled
        if (self.ui.MediaPlayerState=='false'):
            self.log.info('No Media Player is selected. Use Settings Menu to set a player')
            return
        
        self.tokenList = []
        self.recursivePath = ""
        #Now we need to recursively traverse till we reach the root
        
        #get the current widget item
        self.__recursiveSearch__(self.sender().currentItem())
        #Now from the token list reading backwards form the complete path
        completePath = self.libraryPath
        for tokenText in reversed(self.tokenList):
            completePath += "/" + tokenText
        self.log.info("Playback path:" + completePath) 
        #Check if the video is not already queued
        if self.sender().currentItem().getQueuedStatus() == False:
            #Change text color
            self.sender().currentItem().setTextColor(0, QtGui.QColor("blue"))
            #Also change its state
            self.sender().currentItem().setQueuedStatus(True)
            #Added for multi playback of all the nodes if the parent is clicked
            #Get the number of children
            childrenCount = self.sender().currentItem().childCount()
            if childrenCount > 0:
                #Iterate through all the children and make their icon to state play
                for i in range (0, childrenCount):
                    #Get the child item
                    childNode = self.sender().currentItem().child(i)
                    #Change its icon
                    childNode.setIcon(0, QtGui.QIcon(QtCore.QString("./resources/playVideo.gif")))
                    #And also the font color
                    childNode.setTextColor(0, QtGui.QColor("blue"))
                #Also keep the nodes expanded
                self.sender().currentItem().setExpanded(True)
                #Hack here - call the tree widget to expand all
#                self.sender().currentItem().treeWidget().expandAll()
            completePath = completePath.replace('/', '\\')
            self.log.info("Path:" + completePath)
            #Change the icon for this node indicating it is queued
            self.sender().currentItem().setIcon(0, QtGui.QIcon(QtCore.QString("./resources/playVideo.gif")))
            #Begin Playback
            VlcPlayer(self,completePath, self.vlcPath)
            
#    def addDirectLinkSlot(self):
#            #also create a new row
#            self.ui.textEdit_2.insertRow(1)
#            #Also add button
#            self.ui.addLinkButton2 = QtGui.QPushButton();
#            self.ui.addLinkButton2.setFlat(True)
#            self.ui.addLinkButton2.setAutoFillBackground(True)
#            self.ui.addLinkButton2.setIcon(QtGui.QIcon(QtCore.QString("./resources/add.gif")))
#            
#            self.ui.textEdit_2.setCellWidget(1,2,self.ui.addLinkButton2)
#            QtCore.QObject.connect(self.ui.addLinkButton2, QtCore.SIGNAL("clicked()"), self.addDirectLinkSlot)
        
    def getFilesInDirectory(self, folderName, parent=None):
        '''
        Returns files in the directory
        '''
        try:
            dirList = os.listdir(folderName)
        except:
            #There is some issue in accessing this path, mostly if the folder was deleted and the config hasnt been updated
            #Show the settings dialog
            raise Exception
        for fname in dirList:
            self.log.info(fname)                        
            #Check if this is a directory -http://forums.devshed.com/python-programming-11/recursive-file-search-for-given-extension-519562.html
            if os.path.isdir(os.path.join(folderName, fname)) is True:
                self.log.info('recursively searching in folders')
                treeItemParent = youtube.gui.components.LibraryFileWidgetItem.LibraryFileWidgetItem(QtCore.QStringList(fname))
                treeItemParent.setIcon(0, QtGui.QIcon('./resources/folder.gif'))
                parent.addChild(treeItemParent)
                self.getFilesInDirectory(os.path.join(folderName, fname), treeItemParent)
            elif os.path.isfile(os.path.join(folderName, fname)) is True:
                #Check if the file is a valid FLV
                if os.path.splitext(fname)[1] == '.flv' or os.path.splitext(fname)[1] == '.VOB' or os.path.splitext(fname)[1] == '.MPEG' or os.path.splitext(fname)[1] == '.avi' or os.path.splitext(fname)[1] == '.DAT' or os.path.splitext(fname)[1] == '.mpg' or os.path.splitext(fname)[1] == '.mkv' or os.path.splitext(fname)[1] == '.divx':                
                    #Create a tree item
                    treeItemChild = youtube.gui.components.LibraryFileWidgetItem.LibraryFileWidgetItem(QtCore.QStringList(fname))
                    treeItemChild.setIcon(0, QtGui.QIcon('./resources/song.gif'))
                    #If this is a file add this as a child to its parent
                    parent.addChild(treeItemChild)
                    
    def directDownloadSlot(self):
#            print 'Button clicked:',self.ui.listOfDirectLinkButtons[self.ui.directDownloadLinkButtonCounter -1 ] # -1 as it stores the last pushed button
            print 'button', self.sender()
            #Check if state was Add
            if (self.sender().getAddState() == True):
                print 'Add State'
                if self.ui.lineEdit_3.text() == '':
                    self.totalVideosQueuedForDownload = 1
                    self.ui.lineEdit_3.setText('1')
                else:
                    self.totalVideosQueuedForDownload = self.totalVideosQueuedForDownload + 1
                    self.ui.lineEdit_3.setText(str(self.totalVideosQueuedForDownload))
                self.sender().setAddState(False)
                #Change its icon
                self.sender().setIcon(QtGui.QIcon(QtCore.QString("./resources/delete.gif")))
            else:            
                print 'Removal State:row', self.sender().getButtonCounter()
                if self.ui.lineEdit_3.text() != '':
                    self.totalVideosQueuedForDownload = self.totalVideosQueuedForDownload - 1
                    self.ui.lineEdit_3.setText(str(self.totalVideosQueuedForDownload))
                
                #Remove state - delete this row
                tempRow = self.sender().getButtonCounter()
                self.ui.textEdit_2.removeRow(tempRow)
                self.ui.listOfDirectLinkButtons.remove(self.sender())
                #Shift all other elements below this
                for element in range(0, len(self.ui.listOfDirectLinkButtons)):
                    if self.ui.listOfDirectLinkButtons[element].getButtonCounter() > tempRow:
                        self.ui.listOfDirectLinkButtons[element].setButtonCounter(self.ui.listOfDirectLinkButtons[element].getButtonCounter() - 1)
                
                self.ui.directDownloadLinkButtonCounter = self.ui.directDownloadLinkButtonCounter - 1
                return
            
            #Add another button in a new row
            self.ui.textEdit_2.insertRow(self.ui.textEdit_2.rowCount())
            self.ui.listOfDirectLinkButtons.append(CustomizedDirectDownloadButton(self.ui.directDownloadLinkButtonCounter)) 
            
            self.ui.listOfDirectLinkButtons[self.ui.directDownloadLinkButtonCounter].setFlat(True)
            self.ui.listOfDirectLinkButtons[self.ui.directDownloadLinkButtonCounter].setAutoFillBackground(True)
            self.ui.listOfDirectLinkButtons[self.ui.directDownloadLinkButtonCounter].setIcon(QtGui.QIcon(QtCore.QString("./resources/add.gif")))
            self.ui.textEdit_2.setCellWidget(self.ui.directDownloadLinkButtonCounter, 2, self.ui.listOfDirectLinkButtons[self.ui.directDownloadLinkButtonCounter])
                   
            QtCore.QObject.connect(self.ui.listOfDirectLinkButtons[self.ui.directDownloadLinkButtonCounter], QtCore.SIGNAL("clicked()"), self.directDownloadSlot)
    #        self.listOfDirectLinkButtons.append(self.listOfDirectLinkButtons[self.directDownloadLinkButtonCounter])
            self.ui.directDownloadLinkButtonCounter = self.ui.directDownloadLinkButtonCounter + 1 
            
                            

    def checkBoxSlot(self, i):
        '''Slot that handles check box press event'''
        # IMP - This gives us the reference of the sender - which checkBox was pressed and text identifies the checkBox index from the array
        videoInformationIndex = int((self.sender()).getNumberIndex())        
        #Check if the user checked it - can also be unchecked 
        if self.sender().checkState() == QtCore.Qt.Checked:
            self.totalVideosQueuedForDownload = self.totalVideosQueuedForDownload + 1
            self.videoList[self.ui.videoList[videoInformationIndex - 1].getTitle()] = self.ui.videoList[videoInformationIndex - 1].getWebPageUrl()
        else:
            self.totalVideosQueuedForDownload = self.totalVideosQueuedForDownload - 1
            #Remove this from the dictionary
            del self.videoList[self.ui.videoList[videoInformationIndex - 1].getTitle()]             
        self.log.info('Size of Download List:' + str(len(self.videoList)))
        #Update the status line edit
        self.ui.lineEdit_3.setText(str(self.totalVideosQueuedForDownload))
        videoInformationIndex = videoInformationIndex - 1
        # Once checked, display the corresponding web page URL on the text edit for downloading
        (self.ui.textEdit).append(QString(self.ui.videoList[videoInformationIndex].getWebPageUrl()))
        #Sets up the video index in the line edit which shows the video information#            (self.ui.lineEdit_2).setText(str(videoInformationIndex+1))
        # Display Video Title
        (self.ui.label_4).setText(" " + self.ui.videoList[videoInformationIndex].getTitle())
        # Convert time and then display
        self.convertTimeInSec(int(self.ui.videoList[videoInformationIndex].getDuration()))
        self.duration = ""
        if(self.hrs is not 0):
            self.duration = self.duration + "Hrs: " + str(self.hrs) + " "
        elif(self.mins is not 0):
            self.duration = self.duration + "Mins: " + str(self.mins) + " "
        self.duration = self.duration + "Sec: " + str(self.sec)
        (self.ui.label_6).setText(self.duration)# Display Time in Hrs,Mins and Sec
        (self.ui.label_8).setText(self.ui.videoList[videoInformationIndex].getCategory())#Display Category
        (self.ui.label_10).setText(self.ui.videoList[videoInformationIndex].getDate())#Display publishing date
    
    def getHours(self):
        '''
        Returns hours
        '''
        return self.hrs
    
    def getMins(self):
        '''
        Return Minutes
        '''
        return self.mins
    
    def getSeconds(self):
        '''
        Return Seconds
        '''
        return self.sec

    def beginDownload(self):        
        '''This method creates a thread to begin downloading of the list of videos
        as selected by the user'''     
        #Check if we have some direct links
        columns = self.ui.textEdit_2.columnCount()
        rows = self.ui.textEdit_2.rowCount()
        columns = columns - 2
        list = []
        for i in range(0, rows):
            for j in range(0, columns):
                tableWidgetItem = self.ui.textEdit_2.item(i, j)
                tableWidgetItemNext = self.ui.textEdit_2.item(i, j + 1)
                if tableWidgetItem != None and tableWidgetItemNext != None and tableWidgetItem.text() != '' and tableWidgetItemNext.text() != '':
                    print tableWidgetItem.text()
                    self.videoList[str(tableWidgetItem.text())] = str(tableWidgetItemNext.text()) 
                    list.append(tableWidgetItem)
        if len(list) == 0:
            print 'No Direct Download Link Found'
        
        self.log.info("Download Video Itenary:" + str(self.videoList))
        #check if there is anything to download
        if len(self.videoList) != 0:
            self.downloadVideosCompletedUpdate(0)           
            self.obj = youtube.util.downloader.GenericDownloader.NewDownloader(self, self.videoList)
            #Updates from downloader thread
            QtCore.QObject.connect(self.obj, QtCore.SIGNAL('download_completed()'), self.updateVideoLibrary)
            #Progress update
            QtCore.QObject.connect(self.obj, QtCore.SIGNAL('progress_update(int)'), self.downloadProgressUpdate)
            #Videos completed signal
            QtCore.QObject.connect(self.obj, QtCore.SIGNAL('video_downloaded(int)'), self.downloadVideosCompletedUpdate)
            self.obj.start()
            #Also disable download button
            self.ui.pushButton_4.setEnabled(False)
        else:
            self.log.info("Downloader found nothing to download")
    def downloadVideosCompletedUpdate(self, value):
        '''
        Updates label with number of videos completed after a download
        '''
        
        self.ui.labelDownloadStatus.setText(str(value) + ' Of ' + str(len(self.videoList)))
        #Check if we have downloaded all videos
        if value == len(self.videoList):
            self.ui.pushButton_4.setEnabled(True)           
            #Also reset all the checked boxes
            for i in range(0, len(self.ui.checkBoxesArray)):
                if self.ui.checkBoxesArray[i].checkState() == QtCore.Qt.Checked:
                    self.ui.checkBoxesArray[i].setCheckState(QtCore.Qt.Unchecked)
            #Also clear the videolist
            self.videoList.clear()
            self.ui.lineEdit_3.setText('')
    def downloadProgressUpdate(self, value):
        '''
        Update download progress bar
        '''
        self.ui.progressBar.setValue(value)
   
    def flushBeforeExit(self):
        '''
        This method dumps the logs into its appropriate log file
        '''
        self.log.info("Quitting")
        try:
            #Over here log all information in a log file
            if not os.path.exists('./Logs'):
                os.makedirs('./Logs')
            logFile = open('./Logs/LogFile.txt', 'a')
            logFile.write(self.loggingHandler.getLoggingCompleteText())
            logFile.close()
        except:
            pass
    def exitActionSlot(self):
        '''
        Slot Handler for Exit 
        '''
        self.flushBeforeExit()        
        myapp.close()    
                                     
    def openBrowser(self, link):
        '''This opens the default browser with the video as requested'''
        webbrowser.open(link)

    def convertTimeInSec(self, sec):
        '''This converts given time in seconds into hrs,mins and sec'''
        self.hrs = int(sec / 3600)
        if(self.hrs is not 0):
            secElapsed = self.hrs * 60 * 60
        else:
            secElapsed = 0
        self.mins = int((sec - secElapsed) / 60)
        if(self.mins is not 0):
            secElapsed2 = self.mins * 60
        else:
            secElapsed2 = 0
        self.sec = sec - secElapsed - secElapsed2

if __name__ == "__main__":
    #This is necessary for Py2exe redirection of exceptions, otherwise a dialog is shown notifying of an error log
    try:
        if not os.path.exists('./Logs'):
            os.makedirs('./Logs')
        sys.stdout = open('./Logs/Exceptions', 'a')
        sys.stderr = open('./Logs/Exceptions', 'a') 
    except:
        pass      
    print "Running Video Download Assistant v2.1"
    app = QtGui.QApplication(sys.argv)
    #create the splash screen
    splash = QSplashScreen() 
    #create a progress bar
    progressBar = QProgressBar(splash)
    img = QImage("./Resources/splash.jpg") 
    pm = QPixmap.fromImage(img) 
    if not pm.mask(): 
        if img.hasAlphaBuffer(): bm = img.createAlphaMask() 
        else: bm = img.createHeuristicMask() 
        pm.setMask(bm) 
    if pm.mask(): splash.setMask(pm.mask()) 
    splash.setPixmap(pm) 
    #Set the geometry
    progressBar.setGeometry(splash.width() / 20, splash.height() / 10,
                        splash.width() - 18, splash.height() / 12)
    splash.show() 
    app.processEvents()
    myapp = StartMainWidget()
    splash.finish(myapp.show())
    sys.exit(app.exec_())
