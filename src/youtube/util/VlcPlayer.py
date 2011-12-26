'''Testing License v0.1'''
'''
Created on Feb 14, 2010

@author: Rahul Sinha
'''
import subprocess
import os
class VlcPlayer(object):
    '''
    classdocs - This class invokes an external VLC instance
    The location is specified in the configuration.xml
    and can also be changed from the main window
    '''


    def __init__(self,parent, videoFilePath, vlcPath):
        '''
        Constructor - Damn i had lots of trouble using VLC path having several spaces
        and also the library file
        Also See - http://coding.derkeiler.com/Archive/Python/comp.lang.python/2008-03/msg01930.html
        '''
        try:
            fileName = os.path.abspath(videoFilePath)
            print fileName
            print 'Playing:', vlcPath + '"' + fileName + '"'
            vlcExecCommandString = r'"' + vlcPath + ' "'
            print "VLC Exec String:", vlcExecCommandString
    #        process = subprocess.Popen('c:\\progra~1\\VideoLAN\VLC\\vlc.exe "'+fileName+'"'+' --one-instance --playlist-enqueue', shell=True, stdout=subprocess.PIPE)
            libraryFileString = r'"' + videoFilePath + '"'
            print "Library Video Path:", libraryFileString
            print "Complete Command:", vlcExecCommandString + libraryFileString
            process = subprocess.Popen(str(vlcExecCommandString) + str(libraryFileString) + ' --one-instance --playlist-enqueue', stdout=subprocess.PIPE)
        
        except:
            #For any exceptions display settings dialog
            parent.showSettingsDialogSlot()