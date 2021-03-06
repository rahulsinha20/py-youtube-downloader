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
XML reading/writing facility
It reads from a configuration file and sets up application properties accordingly
The default file used is /Resources/configuration.xml
@author: Rahul Sinha
'''
from xml.dom.minidom import parse
import xml
class PropertiesAccessor(object):
    '''
    classdocs - this class writes user specified properties as
    an xml and reads them for application configuration
    '''
    def __init__(self, propertiesFile='./Resources/configuration.xml'):
        '''
        Constructor
        '''
        self.propertiesFile = propertiesFile
        self.libraryPath = ''
        self.vlcPath = ''
        self.MediaPlayerEnabled = ''
        self.embeddedVideosEnabled = ''
        #Constants
        self.MEDIAPLAYERENABLED = 'mediaplayer-enabled'
        self.LIBRARY_LOCATION = "library-location"
        self.VLC_LOCATION = "vlc-location"
        self.EMBEDDEDVIDEOSENABLED = 'embedded-videos-enabled'
    def write(self, libraryLocation, vlcLocation, mediaplayerEnabled="true", embeddedVidsEnabled = "true"):
        '''
        This is where we dump the app configurations
        into an xml file
        '''
        #Create a Document instance
        doc = xml.dom.minidom.Document() #@UndefinedVariable
        #Create an element for this doc
        appSettingNode = doc.createElement("App-Settings")
        #Add this element as a child to the Root document
        doc.appendChild(appSettingNode)
        #Create an element to store library location
        libNode = doc.createElement('library-location')
        appSettingNode.appendChild(libNode)
        #Store the lib location in this node
        libLocationTextNode = doc.createTextNode(libraryLocation)
        #Append this as a child to library location node
        libNode.appendChild(libLocationTextNode)
        
        # Create a new node to store mediaplayer-enabled
        mediaplayerenabledNode=doc.createElement('mediaplayer-enabled')
        libNode.appendChild(mediaplayerenabledNode)
        #Create a text node to store the value
        mediaplayerEnabledTextNode = doc.createTextNode(mediaplayerEnabled)
        #Add this as a child to the upper node
        mediaplayerenabledNode.appendChild(mediaplayerEnabledTextNode)
        
        #Create a node to store VLC location
        vlcLocationNode = doc.createElement('vlc-location')
        mediaplayerenabledNode.appendChild(vlcLocationNode)
        #Create a text node to store the value
        vlcLocationTextNode = doc.createTextNode(vlcLocation)
        #Add this as a child to the VLC location node
        vlcLocationNode.appendChild(vlcLocationTextNode)
        
        #Create a node to indicated if embedded videos are allowed
        embeddedVideosEnabledNode = doc.createElement('embedded-videos-enabled')
        vlcLocationNode.appendChild(embeddedVideosEnabledNode)
        #Create a text node to store the value
        embeddedVideosEnabledTextNode = doc.createTextNode(embeddedVidsEnabled)
        #Add this as a child to the Embedded Video node
        embeddedVideosEnabledNode.appendChild(embeddedVideosEnabledTextNode)
        

        
        #Now write this to a file in write mode - also erases previous settings
        xmlFileObject = open(self.propertiesFile, "w")
        doc.writexml(xmlFileObject)
        #Close the file handler
        xmlFileObject.close()
    
    def readProperties(self):
        '''
        Reads properties from the config file
        '''        
        #Open XML
        try:
            dom = parse(self.propertiesFile)
        except IOError:
            print 'No Configuration File found'
            return - 1
        self.__readXml(dom)
        
    def __readXml(self, dom):
        '''This is a private method
        see two underscores in the method declaration
        and parses XML
        '''
        for e in dom.childNodes:                          
            if e.nodeType == 3:            
                print e.parentNode.tagName
                if(e.parentNode.tagName == self.LIBRARY_LOCATION):
                    self.libraryPath = e.nodeValue
                    print e.nodeValue
                    continue
                elif(e.parentNode.tagName == self.VLC_LOCATION):
                    self.vlcPath = e.nodeValue
                    print e.nodeValue
                    continue
                elif(e.parentNode.tagName == self.MEDIAPLAYERENABLED):
                    self.MediaPlayerEnabled = e.nodeValue
                    print e.nodeValue
                    continue
                elif(e.parentNode.tagName == self.EMBEDDEDVIDEOSENABLED):
                    self.embeddedVideosEnabled = e.nodeValue
                    print e.nodeValue
                    continue
            self.__readXml(e)
            
    def getEmbeddedVideosEnabled(self):
        '''
        Returns if Embedded Player is enabled
        '''    
        return self.embeddedVideosEnabled
           
    def getMediaPlayerEnabled(self):
        '''
        Returns if media player is enabled
        '''    
        return self.MediaPlayerEnabled
    
    def getLibraryPath(self):
        '''
        Return the parsed library path
        '''
        return self.libraryPath
    
    def getVlcPath(self):
        '''
        Return parsed VLC path
        '''
        return self.vlcPath
        
