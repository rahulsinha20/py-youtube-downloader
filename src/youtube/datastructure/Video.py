'''
Created on Feb 28, 2010
@author: Rahul Sinha
'''

class Video(object):
    '''
    classdocs
    This class represents a Video entity as extracted from the video services
    '''
    def __init__(self):
        '''
        Constructor - sets up default values for attributes
        '''
        self.title = ''
        self.thumbnails = []
        self.webPageUrl = ''
        self.duration = 0
        self.category = ''
        self.date = ''
        self.embedLink = ''
        self.videoNumber = 0
        self.source = ''
        
    def setSource(self, source):
        '''
        Sets source for the video {YouTube,Metacade,Dailymotion etc}
        '''
        self.source = source
        
    def setVideoNumber(self, number):
        '''
        Sets the video number
        '''
        self.videoNumber = number
        
    def setTitle(self, title):
        '''
        Sets video title
        '''
        self.title = title
    
    def setEmbedLink(self, embedLink):
        '''
        Sets Embedded Link
        '''
        self.embedLink = embedLink
            
    def setThumbnails(self, thumbnails):
        '''
        Sets thumbnails
        '''
        self.thumbnails = thumbnails
    
    def setWebPageUrl(self, webPageUrl):
        '''
        Sets web page url
        '''
        self.webPageUrl = webPageUrl
        
    def setDuration(self, duration):
        '''
        Sets video duration
        '''
        self.duration = duration
        
    def setCategory(self, category):
        '''
        Sets video category
        '''
        self.category = category
    
    def setDate(self, date):
        '''
        Sets video publishing date
        '''
        self.date = date
        
    # Now defining accessors

    def getSource(self):
        '''
        Returns video source
        '''
        return self.source
    
    def getVideoNumber(self):
        '''
        Returns video number
        '''
        return self.videoNumber
    

    
    def getTitle(self):
        '''
        Returns video title
        '''
        return self.title
    
    def getThumbnails(self):
        '''
        Returns thumbnails
        '''
        return self.thumbnails
    
    def getWebPageUrl(self):
        '''
        Returns web page url
        '''
        return self.webPageUrl
    
    def getDuration(self):
        '''
        returns video duration
        '''
        return self.duration
    
    def getCategory(self):
        '''
        Returns video category
        '''
        return self.category
    
    def getDate(self):
        '''
        returns video date
        '''
        return self.date
    def getEmbedLink(self):
        '''
        Returns embedded link
        '''
        return self.embedLink
        
