'''Testing License v0.1'''
'''
Created on Jun 29, 2009
This is my first attempt with OO Python!
Based on: http://www.catonmat.net/blog/downloading-youtube-videos-with-a-perl-one-liner/
Adapted from: http://www.computerhope.com/forum/index.php?topic=82205.0
@author: Rahul Sinha
'''
import urllib
import os
import urllib2
import threading
from PyQt4.QtCore import QString

class Downloader(threading.Thread):
    '''
    This class provides downloading of youtube videos provided with a URL
    It is implemented as a Thread, the main functionalities are provided 
    within the run method
    '''
    
    def __init__(self, parent, videoList):
        '''
       This is the non default constructor
       self.searchText - is used to make parent directory
       and all videos present in the list are downloaded in the folder
        '''
        threading.Thread.__init__(self) # Call the Parent constructor
        self.parent = parent # Store the reference of the class that created me
        self.videoItenary = videoList #Dictionary of videos to be downloaded
        self.numberOfVideos = len(self.videoItenary) 
        #Check if Search keyword is enabled
        if parent.ui.lineEdit.isEnabled() == True:
            self.searchText = str(parent.ui.lineEdit.text())
        else:
            self.searchText = ''
        self.fileTitle = 'NoTitle'

    def run(self):
        '''
        This is the run method for the Thread
        It performs reading the YouTube URLs from the video itenary list, opening the stream
        connecting to the URLs and then extracting the download parameters. This is then
        used to perform Download of the required videos
        '''   
        running = True # I am now running
        index = 0 # Keep track of the number of videos downloaded
        while running:
            if(index == self.numberOfVideos): # If all videos are downloaded
                (self.parent.ui.textEdit).append(QString("[ I ] - Completed Downloading " + str(index) + " Videos!"))
                running = False   # Change state to non-running
                break # break from the loop
            # For videos download display appropriate messages on the console - using parent reference
#            self.parent.ui.label_3.setText("Status: Downloading: "+str(index+1)+" Of "+str(self.numberOfVideos))
            # Set parent UI progress bar to 0
            (self.parent.ui.progressBar).setValue(0)
            consoleStr = QString("[ I ] - Requested URL: " + (self.videoItenary.values()[index]))
            (self.parent.ui.textEdit).append(consoleStr)
            self.refresh()  # Refresh parent UI Widget (Not Working)
            self.openURL(str(self.videoItenary.values()[index])) # Open URL
            #commented below for new utube changes 10/11/10
            #self.constructVideoParams() # Construct Video Parameters - For reference see /resources/UTubeVideoParamTutorial.txt
            self.constructVideoParamsSep2010()
            self.fileTitle = self.videoItenary.keys()[index]
#            self.download() # Begin Download
            self.downloadSep2010()
            index = index + 1
            downloadStatus = QString("[ I ] - Download Status: " + str(index) + " Of " + str(self.numberOfVideos))
            (self.parent.ui.textEdit).append(downloadStatus) 
            self.refresh()
#        (self.parent.ui.label_3).setText("Status: Idle")
            #Now request parent to upload library
        self.parent.updateVideoLibrary()
          
    
    def openURL(self, url):
        ''' This method opens up a URL Connection with the remote site
        as identified by the URL
        '''
        (self.parent.ui.textEdit).append(QString("[ I ] - Trying to open URL:" + str(url)))
        self.refresh()
        # Try to open a streaming connection to the URL, catch all the exceptions and display on the parent UI
        try:
            self.urlStream = urllib.urlopen(url)
        except Exception, e:
            (self.parent.ui.textEdit).append(QString("[ E ] - Error: " + str(e)))
              

    def constructVideoParams(self):
        ''' This method is responsible to create the required Video Parameters
        which are needed to download a Youtube video
        '''
        (self.parent.ui.textEdit).append(QString("[ I ] - Page Read Complete"))
        self.refresh()
        try:
            # Read the Page
            self.page = self.urlStream.read()
            # In order to get the embedded FLV Parameter, we need to extract the strings from
            # the above acquired page through the stream
            
            #NOTE - Due to recent changes and support to other media, youtube has changed these parameters
            #and hence we comment out the next line as instead of var swfArgs it consists of SWF_ARGS (11/02/10)
#            self.startIndex=self.page.index("var swfArgs")
            self.startIndex = self.page.index("SWF_ARGS")            
            self.videoParams = self.page[self.startIndex:]
#            self.endIndex=self.videoParams.index("};")
            self.endIndex = self.videoParams.index("});") #Changed 11/02/10
            self.videoParams = self.videoParams[:self.endIndex]
            self.videoParams = self.videoParams.split(",")
            #(self.parent.ui.plainTextEdit_2).appendPlainText(QString("[ D ] - "+str(self.videoParams)))
            # With the split function the extracted string for swfArgs is rendered
            # as list of words - Split example is provided with this package
        except Exception, e:
            (self.parent.ui.textEdit).append(QString("[ E ] - Error: " + str(e)))

        
        
    def constructVideoParamsSep2010(self):
        (self.parent.ui.textEdit).append(QString("[ I ] - Page Read Complete"))
        self.refresh()
        try:
            # Read the Page
            self.page = self.urlStream.read()
            # find index for "img.src = "
            self.startIndex = self.page.index("img.src = ")
            self.videoParams = self.page[self.startIndex + len("img.src = "):]
            self.endIndex = self.videoParams.index(";") #Changed 11/09/10
            self.videoParams = self.videoParams[:self.endIndex]
            #replace generate_204 with videoplayback
            self.videoParams = self.videoParams.replace("generate_204", "videoplayback")
            self.videoParams = self.videoParams.replace("\\/", "/")
            
            print "VIDEO PARAMS:", self.videoParams
        except Exception, e:
            (self.parent.ui.textEdit).append(QString("[ E ] - Error: " + str(e)))
            
    def downloadSep2010(self):
        ''' This method begins downloading of youtube videos by making
        use of the constructed list of video arguments
        '''
        #self.downloadDict={} # Matches key and value pair
        try:
#            for line in self.videoParams:
#                # From the list of words the important fields are (1) Video_id (2) t
#                # We scan the words to find either of them
#                if "video_id" in line or "\"t\"" in line:
#                    # We take off the quotes from "video_id": "UC-RFFIMXlA" and then split at :
#                    # and store them in two variables
#                    v,vnum=line.replace("\"","").split(":")
#                    # We can then use a dictionary to store these values with key as video_id and values as UC-RF....
#                    self.downloadDict[v.strip()]=vnum.strip()
            self.downloadLink = self.videoParams
        except Exception, e:
            (self.parent.ui.textEdit).append(QString("[ E ] - Error: " + str(e)))
        # Create a directory to store downloaded videos
        try:
            if self.searchText != '':
                downloadPath = self.parent.getLibraryPath() + "/" + self.searchText
            else:
                downloadPath = self.parent.getLibraryPath() + "/" + str(self.parent.ui.comboBox.currentText())
            os.makedirs(downloadPath)
        except OSError:
            pass
        # Begin downloading the file and store it on local machine
        # The destination filename is created using epoch
        try:
#            destinationFileName=self.searchText+"_"+str(int(time.time()))+".flv"
            destinationFileName = self.fileTitle + ".flv"
            # Display appropriate messages on paremt UI
            (self.parent.ui.textEdit).append(QString("[ I ] - Now Downloading...."))
            (self.parent.ui.textEdit).append(QString("[ D ] - Download Link: " + str(self.downloadLink)))
            (self.parent.ui.textEdit).append(QString("[ I ] - Local File Name: " + destinationFileName))
            self.refresh()
            print "Downloading:", str(self.downloadLink)
            print "Destination:", destinationFileName
            # Begin Retrieving the video - With a report Hook
            # Report Hook is used to update the progress of download on the progress bar
            # For more information see the reporthook method
            fp = open(downloadPath + "/" + destinationFileName, "w")
            req = urllib2.urlopen(self.downloadLink)
            for line in req:
                fp.write(line)
            fp.close()
#            webFile=urllib.urlretrieve(urllib.urleself.downloadLink,downloadPath+"/"+destinationFileName,reporthook=self.reporthook)
            (self.parent.ui.textEdit).append(QString("[ I ] - Download Complete"))
        except Exception, e:
            (self.parent.ui.textEdit).append(QString("[ E ] - Error: " + str(e)))


        
    def download(self):
        ''' This method begins downloading of youtube videos by making
        use of the constructed list of video arguments
        '''
        self.downloadDict = {} # Matches key and value pair
        try:
            for line in self.videoParams:
                # From the list of words the important fields are (1) Video_id (2) t
                # We scan the words to find either of them
                if "video_id" in line or "\"t\"" in line:
                    # We take off the quotes from "video_id": "UC-RFFIMXlA" and then split at :
                    # and store them in two variables
                    v, vnum = line.replace("\"", "").split(":")
                    # We can then use a dictionary to store these values with key as video_id and values as UC-RF....
                    self.downloadDict[v.strip()] = vnum.strip()
            self.downloadLink = "http://www.youtube.com/get_video?video_id=%s&t=%s" % (self.downloadDict['video_id'], self.downloadDict['t'])
        except Exception, e:
            (self.parent.ui.textEdit).append(QString("[ E ] - Error: " + str(e)))
        # Create a directory to store downloaded videos
        try:
            if self.searchText != '':
                downloadPath = self.parent.getLibraryPath() + "/" + self.searchText
            else:
                downloadPath = self.parent.getLibraryPath() + "/" + str(self.parent.ui.comboBox.currentText())
            os.makedirs(downloadPath)
        except OSError:
            pass
        # Begin downloading the file and store it on local machine
        # The destination filename is created using epoch
        try:
#            destinationFileName=self.searchText+"_"+str(int(time.time()))+".flv"
            destinationFileName = self.fileTitle + ".flv"
            # Display appropriate messages on paremt UI
            (self.parent.ui.textEdit).append(QString("[ I ] - Now Downloading...."))
            (self.parent.ui.textEdit).append(QString("[ D ] - Download Link: " + str(self.downloadLink)))
            (self.parent.ui.textEdit).append(QString("[ I ] - Local File Name: " + destinationFileName))
            self.refresh()
            # Begin Retrieving the video - With a report Hook
            # Report Hook is used to update the progress of download on the progress bar
            # For more information see the reporthook method
            webFile = urllib.urlretrieve(self.downloadLink, downloadPath + "/" + destinationFileName, reporthook=self.reporthook)
            (self.parent.ui.textEdit).append(QString("[ I ] - Download Complete"))
        except Exception, e:
            (self.parent.ui.textEdit).append(QString("[ E ] - Error: " + str(e)))

    def reporthook(self, blocks_read, block_size, total_size):
        ''' This is the report Hook method that is used to show the progress
        of video retrievals on the progress bar. The parameters are the:
        (1) Number of Blocks Read
        (2) Size of Each Block
        (3) Size of the File
        Using above three we can calculate the percentage of file downloaded
        '''
        if not blocks_read:
            #nothing to do here
            return
        if total_size < 0:
        # Unknown size
            print 'Read %d blocks' % blocks_read
        else:
            amount_read = blocks_read * block_size
            #print 'Read %d blocks, or %d/%d' % (blocks_read, amount_read, total_size)
            # Compute the percentage of video downloaded
            (self.parent.ui.progressBar).setValue((float(amount_read) / float(total_size)) * 100)
        return
            
    def refresh(self):
        ''' Refreshes the Parent UI Widget '''
        (self.parent.ui.textEdit).update()
    
