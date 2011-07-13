# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoDownloader.ui'
#
# Created: Wed Feb 17 21:41:59 2010
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtNetwork, Qt
from AboutAuthor import Ui_Dialog
import urllib
import youtube.gui.util.SettingsDialog
import os
from youtube.gui.util.CustomizedDirectDownloadButton import CustomizedDirectDownloadButton
from youtube.gui.util.CustomizedCheckBox import NumberedCheckBox
from youtube.gui.util.ClickableLabel import ClickableLabel



class Ui_MainWindow(object):
    def refreshWidget(self, thumbs, webPageUrl, titleList, durationList, categoryList, dateList, mediaLink):
        '''This method retrieves the video information from the VideoSearch class. Parameters are
        (1)thumbs - List of video thumbnails
        (2)webPageUrl - List of web page urls for the videos
        (3)titleList - List of video Titles
        (4)durationList - List of video duration (in seconds)
        (5)categoryList - List of video Categories
        (6)dateList - List of publishing Date for the videos
        (7) Media Link - useful for embedding videos
        '''   
        self.elements = len(thumbs)
        self.webPageUrl = webPageUrl
        self.thumbLinks = thumbs
        self.titleList = titleList
        self.durationList = durationList
        self.categoryList = categoryList
        self.dateList = dateList
        #self.downloadThumbnails()
        self.addWidgetOnLayout()  
        #Added 18/02/2010
        self.mediaLink = mediaLink    

    def receiveVideoListcallback(self, videoList):
        '''
        This callback method receives list of videos after they have been queried from
        the web services
        Added 28/02/10        
        '''
        #Dispose the search progress bar
        
        self.videoList = videoList;
        #Once we receive update, we add them on the widget - i.e show video lists
        self.addWidgetOnLayout()  
    def UpdateEmbeddedVideoState(self, state):
        '''
        Updates embedded video state
        '''   
        self.EmbeddedVideoState = state
    def UpdateMediaPlayerState(self, state):
        '''
        Sets Media Player state
        '''
        self.MediaPlayerState = state
            
    def setupUi(self, MainWindow):
        self.UILauncher = MainWindow
        #set flags to indicate state for embeded videos
        self.EmbeddedVideoState = self.UILauncher.properties.getEmbeddedVideosEnabled()
        #set flags to indicate whether media player is enabled
        self.MediaPlayerState = self.UILauncher.properties.getMediaPlayerEnabled()
        #Instantiate settings dialog with parent as the main window
        self.settingsDialog = youtube.gui.util.SettingsDialog.Ui_Dialog(MainWindow)
        #About Author
        self.aboutAuthorDialog = Ui_Dialog(MainWindow)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1277, 717)
        #Disable Maximize
        MainWindow.setWindowFlags(Qt.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        font1 = QtGui.QFont()
        font1.setBold(True);
        
#        self.groupBox.setStyle()
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 471, 541))
        self.groupBox.setObjectName("groupBox")
       
        
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_4 = QtGui.QScrollArea(self.groupBox)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtGui.QWidget(self.scrollArea_4)
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 449, 506))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_8.addLayout(self.gridLayout)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout.addWidget(self.scrollArea_4)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 251, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 171, 16))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(120, 50, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 10, 201, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 151, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 46, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(60, 40, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(60, 60, 131, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(80, 80, 111, 16))
        self.label_10.setObjectName("label_10")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(490, 10, 421, 351))
        self.groupBox_4.setObjectName("groupBox_4")
        self.webView = QtWebKit.QWebView(self.groupBox_4)
        self.webView.setGeometry(QtCore.QRect(10, 20, 401, 321))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(940, 640, 81, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(1022, 640, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1230, 640, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(920, 10, 351, 611))
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtGui.QScrollArea(self.groupBox_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 576))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget = QtGui.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "")
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(490, 370, 421, 301))
        self.groupBox_6.setObjectName("groupBox_6")
        self.tabWidget = QtGui.QTabWidget(self.groupBox_6)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 401, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea_2 = QtGui.QScrollArea(self.tab)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget(self.scrollArea_2)
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 375, 195))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_5.addWidget(self.textEdit)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab, QtGui.QIcon(QtCore.QString("./resources/console.gif")), "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollArea_3 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget(self.scrollArea_3)
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 98, 77))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        #QTableWidget
        self.textEdit_2 = QtGui.QTableWidget(self.scrollAreaWidgetContents_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setColumnCount(3)
        self.textEdit_2.setRowCount(1)
        #Set column width
        self.textEdit_2.setColumnWidth(0, 90)
        self.textEdit_2.setColumnWidth(1, 225)
        self.textEdit_2.setColumnWidth(2, 40)
        self.headerList = QtCore.QStringList()
        self.headerList.append('Title')
        self.headerList.append('Link')
        self.headerList.append('Add')
        self.textEdit_2.setHorizontalHeaderLabels(self.headerList)
        self.textEdit_2.verticalHeader().hide()
        #Create a list of QPUshButtons
        self.listOfDirectLinkButtons = []
        self.directDownloadLinkButtonCounter = 0
        addLinkButton = CustomizedDirectDownloadButton(self.directDownloadLinkButtonCounter)
        addLinkButton.setFlat(True)
        addLinkButton.setAutoFillBackground(True)
        addLinkButton.setIcon(QtGui.QIcon(QtCore.QString("./resources/add.gif")))
        self.textEdit_2.setCellWidget(self.directDownloadLinkButtonCounter, 2, addLinkButton)
        self.directDownloadLinkButtonCounter = self.directDownloadLinkButtonCounter + 1
        #For direct download link
        QtCore.QObject.connect(addLinkButton, QtCore.SIGNAL("clicked()"), MainWindow.directDownloadSlot)
        self.listOfDirectLinkButtons.append(addLinkButton)
        self.horizontalLayout_6.addWidget(self.textEdit_2)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_7.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.tab_2, QtGui.QIcon(QtCore.QString("./resources/directVideoLink.gif")), "")
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 270, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.labelDownloadStatus = QtGui.QLabel(self.groupBox_6)
        self.labelDownloadStatus.setGeometry(QtCore.QRect(360, 270, 75, 23))
        self.labelDownloadStatus.setText('Waiting')
        self.label_12 = QtGui.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(10, 270, 81, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 270, 41, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.progressMainStyle = """
            QProgressBar {
                text-align: center;                
            }"""

        self.progressBar = QtGui.QProgressBar(self.groupBox_6)
        self.progressBar.setGeometry(QtCore.QRect(140, 270, 118, 23))
        self.progressBar.setProperty("value", QtCore.QVariant(0))
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(self.progressMainStyle)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionVideo_Downloader = QtGui.QAction(MainWindow)
        self.actionVideo_Downloader.setObjectName("actionVideo_Downloader")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionVideo_Downloader)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        
        font = QtGui.QFont()
        font.setBold(False)
        
        #Set bold fonts for all the Group Box titles
        self.groupBox.setFont(font1)
        self.groupBox_2.setFont(font1)
        self.groupBox_3.setFont(font1)
        self.groupBox_4.setFont(font1)
        self.groupBox_5.setFont(font1)
        self.groupBox_6.setFont(font1)
        #All labels are not bold
        self.label.setFont(font)
        self.label_10.setFont(font)
        self.label_11.setFont(font)
        self.label_12.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.label_7.setFont(font)
        self.label_8.setFont(font)
        self.label_9.setFont(font)
        #Buttons
        self.pushButton_4.setFont(font)
        self.pushButton_2.setFont(font)
        self.pushButton_3.setFont(font)
        self.pushButton.setFont(font)
        #Combo Box
        self.comboBox.setFont(font)
        #Text Edits
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit_2.setFont(font)
        #Tree Widget
        self.treeWidget.setFont(font)
        #line Edits
        self.lineEdit.setFont(font)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        #Set a default image for web view - ISSUE: IT only works with an absolute path
        # So we form the absolute path and then set that as an html
        imageAbsolutePath = os.getcwd() + "\Resources\DefaultWebKitImage.png"
        htmlTemp = "<br><img src = \"file:///" + imageAbsolutePath + "\"><br></br><b><font size =\"2\" color =\"RED\"> &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;Video Player</font></b>"
        htmlTemp += "<br></br><b><font size =\"2\" color =\"GREEN\"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Click on the selected video for Playback</b>"
        self.webView.setHtml(htmlTemp)
        #WIndow Icon
        MainWindow.setWindowIcon(QtGui.QIcon(QtCore.QString("./resources/app.ico")))
        #Position MainWindow at the center
#        screen = QtGui.QDesktopWidget().screenGeometry()
#        size =  MainWindow.geometry()
#        MainWindow.move((screen.width()-size.width())/2,(screen.height()-size.height()-60)/2)

        #Maximize
#        MainWindow.showMaximized()
        #Network Handles
        self.netManager = QtNetwork.QNetworkAccessManager()
        QtCore.QObject.connect (self.netManager, QtCore.SIGNAL ("finished(QNetworkReply*)"), self.handleNetworkData)
        self.label_defaultPic = QtGui.QLabel()
        self.label_defaultPic.setPixmap(QtGui.QPixmap(QtCore.QString("./resources/youtube.jpg")))
        
        
        #Adding an event handler for pressing return key
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), MainWindow.beginButtonSlot)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), MainWindow.clearButtonSlot)
        
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), MainWindow.beginDownload)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), MainWindow.changeLibraryPath)
#        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), MainWindow.openBrowser)
#        QtCore.QObject.connect(self.actionAuthor, QtCore.SIGNAL("triggered()"), self.openDialog)
        #Exit Action
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.exitActionSlot)
        
        self.addDefaultPic()
        self.populateComboBox()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def addDefaultPic(self):
        self.gridLayout.addWidget(self.label_defaultPic, 0, 0)
        self.defaultSplashScreen = True
    def populateComboBox(self):
        comboBoxEntries = QtCore.QStringList('Select One ...')
        comboBoxEntries.append('Most Viewed')
        comboBoxEntries.append('Top Rated')
        comboBoxEntries.append('Recently Featured')
        comboBoxEntries.append('Most Discussed')
        comboBoxEntries.append('Top Favorites')
        comboBoxEntries.append('Most Responded')
        comboBoxEntries.append('Most Recent')
        self.comboBox.addItems(comboBoxEntries)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "YouTube Video Downloader v2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Videos", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Search Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Enter Video Keyword:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Standard Video Feeds:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Video Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Not Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Duration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Not Applicable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Category:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Not Applicable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Published On:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Not Applicable", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Embedded Video", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Library Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Video Library", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Downloader", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Direct Video Links", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Queued Videos:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVideo_Downloader.setText(QtGui.QApplication.translate("MainWindow", "Video Downloader", None, QtGui.QApplication.UnicodeUTF8))

    def setupLayout(self):
        '''This method setups the layout for the videos to be displayed on the MainWindow
        It uses elementPerRow to divide the layout for each video entry'''
          
        n = 0
        elementPerRow = 3
        self.elements = len(self.videoList)
        rows = self.elements / elementPerRow
        if self.elements % elementPerRow is not 0:
            rows = rows + 1
        self.pos = []
        col = elementPerRow
        # Code below constructs the positional index for components to be displayed
        # on a layout where the number of elements per row is fixed
        # For e.g the positional index if the number of videos obtained are 5 will be
        # [0,0],[0,1][0,2],[1,0],[1,1] where [x,y] x indicates row starting from 0 and y indicates column starting 0
        for i in range(0, rows):
            for j in range (0, col):
                if(n == self.elements):
                    break
                element = [i, j]
                self.pos.append(element)
                n = n + 1
#    def openDialog(self):
#        self.UILauncher.log.info("About");
#
#        self.dlg.show()

    def downloadThumbnails(self):
        '''This method downloads the required thumbnails for the videos. The list of URLs
        pointing to thumbnails are stored in thumbLinks. The images are downloaded to a temporary
        directory named Temp. If not present it is created'''
        # Create a Temporary folder to download the thumbnails
        try:
            os.makedirs("./Temp")
        except OSError:
            pass
        self.names = []
        # Store the thumbnails by downloading them as files into the temporary folder
        fileStr = "Pic"
        i = 0
        # Download the thumbnails
        for j in range(0, len(self.thumbLinks)):
            urllib.urlretrieve(self.thumbLinks[j], "./Temp/" + fileStr + str(i) + ".jpg")
            self.names.append("./Temp/" + fileStr + str(i) + ".jpg")
            i = i + 1
            
    def addWidgetOnLayout(self):
        self.clearWidgetsFromLayout()
        self.setupLayout()
        self.labelArray = []
        self.checkBoxesArray = []
        self.pushButtonArray = []
        self.webLabel = []
        # Add Video information to the layout(Label,CheckBox)
        for i in range(0, self.elements):
#            self.labelArray.append(QtGui.QLabel())
            #Instantiate a label
            clickableLabel = ClickableLabel()            
            self.labelArray.append(clickableLabel)
#            box=QtGui.QCheckBox()
            box = NumberedCheckBox()
            box.setNumberIndex(str(i + 1))
#            box.setText(QtCore.QString(str(i+1)))
            self.checkBoxesArray.append(box)
            self.pushButtonArray.append(QtGui.QPushButton())
        self.acquireImages()
                
    def clear(self):
        '''Clears component texts to default'''
#        (self.plainTextEdit).clear()
#        (self.plainTextEdit_2).clear()
#        (self.label_13).setText("Not Applicable")

    def acquireImages(self):
#        self.j=0
#        for link in self.thumbLinks:
        for video in self.videoList:
            link = video.getThumbnails()
            self.UILauncher.log.info('Acquiring Image:' + link);
            url = QtCore.QUrl(link)
            self.netManager.get (QtNetwork.QNetworkRequest (url))
        #self.gridLayoutWidget.update()
    def clearWidgetsFromLayout(self):
            self.UILauncher.clearVideoList()
#            self.UILauncher.clearDownloadVideoStatus()
            # Delete widgets if they are present on the layout
            # This ensures that videos corresponding to most current search are displayed
            if(self.gridLayout.count() is not 0):
                if (self.defaultSplashScreen is True):
                    self.UILauncher.log.info("Clearing Default Splash Screen")
                    self.gridLayout.removeWidget(self.label_defaultPic)
                    
                    # Just remove does not work we need to call setParent None to each
                    
                    self.label_defaultPic.setParent(None)
                    self.defaultSplashScreen = False
                else:
                    for i in range (0, len(self.checkBoxesArray)):
                        self.gridLayout.removeWidget(self.checkBoxesArray[i])
                        self.gridLayout.removeWidget(self.labelArray[i])
                        # Just remove does not work we need to call setParent None to each
                        self.checkBoxesArray[i].setParent(None)
                        self.labelArray[i].setParent(None)
                self.clear() # Will clear the component texts to default

    def handleNetworkData (self, netReply):
        #qDebug (QString ("Received %1 bytes").arg (netReply.size ()))
        
        img = QtGui.QImage ()
        url = netReply.url ()
        
      #  if netReply.error ():
            #self.filename = QString ()
            #qDebug (QString ("Can't download '%1': %2.").arg (url.toString ()).arg (netReply.errorString()))
       # else:
        thumbUrl = url.toString ()
        self.UILauncher.log.info('Network Reply:' + thumbUrl)
        
            #qDebug (QString ("File '%1' received").arg (self.filename))
        img.load (netReply, None)
        self.UILauncher.log.info('Image Size:(Y)' + str(img.size().height()))
        self.UILauncher.log.info('Image Size:(X)' + str(img.size().width()))  
        #Check if images are larger than expecetd
        if img.size().height() > 90:            
            self.UILauncher.log.info('Height is scaled')
#            largerImgFound=True
            img = img.scaled(img.size().width(), 90, QtCore.Qt.IgnoreAspectRatio)
        if img.size().width() > 120:
            
            self.UILauncher.log.info('Width is scaled') 
#            largerImgFound=True
            img = img.scaled(120, img.size().height(), QtCore.Qt.IgnoreAspectRatio)
        netReply.deleteLater ()
        
        
        self.loadImage (img, thumbUrl)


    def loadImage (self, img, thumbUrl):
        self.UILauncher.log.info("Loading image")
        
        
        #Find which video index this image correspond to
        for videoObj in self.videoList:
            if videoObj.getThumbnails() == thumbUrl:
                self.UILauncher.log.info('Found matching Video for the selected thumbnail')
                self.j = videoObj.getVideoNumber()
                
        
        
        self.labelArray[self.j].setPixmap(QtGui.QPixmap.fromImage(img))
        # Connect a statechanged signal to a slot in the launcher class that calls me
        QtCore.QObject.connect(self.checkBoxesArray[self.j], QtCore.SIGNAL("stateChanged(int)"), self.UILauncher.checkBoxSlot)
        
#        self.labelArray[self.j].setWebLink(self.mediaLink[self.j])
        self.labelArray[self.j].setWebLink((self.videoList[self.j]).getEmbedLink())
        
        #Added 2/12/10 - check if the link is for a truveo video as they can only be played and not downloaded
        #If truveo disable checkbox
        #Modified below as truveo can have video listed from utube also which we can possibly download, using web url rather than embedded
        
#        if (self.videoList[self.j].getEmbedLink()).startswith('http://www.youtube.com')==False:
        if not (((self.videoList[self.j].getWebPageUrl()).startswith('http://www.metacafe.com') == True)or ((self.videoList[self.j].getWebPageUrl()).startswith('http://www.youtube.com') == True) or ((self.videoList[self.j].getWebPageUrl()).startswith('http://www.dailymotion.com') == True)): #or ((self.videoList[self.j].getWebPageUrl()).startswith('http://photobucket.com') == True)): 
#        if (self.videoList[self.j].getWebPageUrl()).startswith('http://www.youtube.com')==False:
            self.checkBoxesArray[self.j].setEnabled(False)
        #Connect a slot to label of images
        QtCore.QObject.connect(self.labelArray[self.j], QtCore.SIGNAL('clicked(PyQt_PyObject)'), self.labelPressed)
#        QtCore.QObject.connect(self.labelArray[self.j], QtCore.SIGNAL('clicked(ClickableLabel)'), self.labelPressed)
        #Give this widget a fixed size
#        self.labelArray[self.j].setFixedSize(200,100)
       
        #Assign a tool tip that contains some descriptive information  
        self.UILauncher.convertTimeInSec(int(self.videoList[self.j].getDuration()))
        hr = self.UILauncher.getHours()
        min = self.UILauncher.getMins()
        sec = self.UILauncher.getSeconds()
        durationInfo = "["
        if (hr != 0):
            durationInfo += str(hr)
            durationInfo += ":"
        durationInfo += str(min) + ":"
        durationInfo += str(sec) + "]"
        
        
        
        
        #Get source for the videos
#        faviconAbsolutePath = os.getcwd() + "\Resources\YouTube_favicon.png"
#        htmlTemp = "<img src=':/Resources/YouTube_favicon.png'>"
        toolTip = "<html><head></head><body bgcolor=\"#E6E6FA\"><span style=\" color:#458B00;\">" + str((self.videoList[self.j]).getTitle()) + "</span><span style=\" color:#FF1493;\">&nbsp;" + durationInfo + '' + (self.videoList[self.j]).getSource()+"</span></body></html>";
        (self.labelArray[self.j]).setToolTip(toolTip);
        self.gridLayout.addWidget(self.labelArray[self.j], self.pos[self.j][0], self.pos[self.j][1])
        self.gridLayout.addWidget(self.checkBoxesArray[self.j], self.pos[self.j][0], self.pos[self.j][1])
        self.j = self.j + 1       
    def labelPressed(self, label):
        '''
        This is where we embed the requested video in the webkit view
        It also enables the plugins from the browser
        Update:13/07/2011: Allowed option to play videos on external browser, this was needed
        as webkit relies on Flash plugin to be installed on Mozilla !
        '''
        link = label.getWebLink()
        if self.EmbeddedVideoState=='true':
            
            #Show a busy cursor            
            QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor);
            websettings = self.webView.settings()
            websettings.setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)
            self.embedVideo(link)
#        
#        
    
#        self.embedVideo(link)
        else:
            self.UILauncher.log.info("Using Default Browser with Embedded Link:" + link)
            self.UILauncher.openBrowser(link)
        
    def embedVideo(self, link):
        self.UILauncher.log.info("Embedded Link:" + link)
        

        html = '<object width="377" height="304"><param name="movie" value=' + link + '&fs=1&"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="' + link + '&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="377" height="304"></embed></object>'
#        html='<object width="377" height="304"><param name="movie" value="http://www.youtube.com/v/JyExxVwTnwg?f=videos&app=youtube_gdata&fs=1&"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/JyExxVwTnwg?f=videos&app=youtube_gdata&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="377" height="304"></embed></object>'
        print 'Embedded link:', html
        
        self.webView.setHtml(html)
        self.webView.show()
    def showSearchProgressBarOnView(self):
        '''
        This shows a progress bar on the view which
        is indeterminate
        '''
        self.progressStyle = """
            QProgressBar {
                background: palette(base);
                border: 2px solid grey;
                border-radius: 5px;
                padding: 0;
            }
            
            QProgressBar::chunk {
                background: palette(highlight);
                background-color: #05B8CC;
                width: 20px;
                
            }"""

        self.progressBarSearch = QtGui.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBarSearch.setToolTip(QtCore.QString("Retrieving Videos"))
        self.progressBarSearch.setMaximum(0)
        self.progressBarSearch.setMinimum(0)
        self.progressBarSearch.setStyleSheet(self.progressStyle)
        self.progressBarSearch.setGeometry(QtCore.QRect(60, 240, 298, 23))
        self.progressBarSearch.show() 
from PyQt4 import QtWebKit
