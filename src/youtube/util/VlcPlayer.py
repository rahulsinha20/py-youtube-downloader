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