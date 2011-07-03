'''
Created on Jun 29, 2009
This class implements functionalities to search YouTube web services for videos
@author: Rahul Sinha
'''
import gdata.youtube.service
import youtube.util.videoservice.TruveoRestClient
import youtube.util.videoservice.MetacafeClient
import youtube.util.videoservice.DailyMotionClient
import youtube.util.videoservice.PhotoBucketClient
import youtube.datastructure.Video
from PyQt4 import QtCore
class VideoSearch(QtCore.QThread):
    '''This class is responsible for invoking the YouTube Web services
    to retrieve all the videos for a keyword'''
          
    def __init__(self, parent=None):
        print 'Thread created'
        QtCore.QThread.__init__(self, parent) # Call the Thread class constructor
             
        
    def begin(self, keyword, standardFeedsActive, feedName):
        '''This method initiates the video search on youtube
        (1)keyword - is the video requested'''
        # Lists to store the video information - Thumbnail,Web URL,Title,Duration,Category and Date
        self.thumbnails = []    
        self.webPageUrl = []
        self.videoTitle = []
        self.videoDuration = []
        self.videoCategory = []
        self.videoDate = []
        #Added 18/02/2010
        self.mediaLink = []
        #Added 28/02/2010
        self.videoList = []
        
        self.feedName = feedName
        self.keyword = keyword
        self.standardFeedsActive = standardFeedsActive
        
    def getVideoCounter(self):
        '''
        Returns Video Counter
        '''
        return self.counter         
    def run(self):
        '''
        Overrides Run method
        '''
        
#        yt_service = gdata.youtube.service.YouTubeService()
        client = gdata.youtube.service.YouTubeService()
        try:
            if self.standardFeedsActive == False:
                try:
                    query = gdata.youtube.service.YouTubeVideoQuery()
                    query.vq = self.keyword
                    query.max_results = '50' # Max videos returned is 50, we are displaying only 25        
                    # Query the youtube web service and populate the above lists
                    feed = client.YouTubeQuery(query)
                except Exception:
                    print 'YouTube client exception'
            else:
                if self.feedName == 'Most Viewed':
                    feed = client.GetMostViewedVideoFeed()
                elif self.feedName == 'Top Rated':
                    feed = client.GetTopRatedVideoFeed()
                elif self.feedName == 'Recently Featured':
                    feed = client.GetRecentlyFeaturedVideoFeed()
                elif self.feedName == 'Most Discussed':
                    feed = client.GetMostDiscussedVideoFeed()
                elif self.feedName == 'Top Favorites':
                    feed = client.GetTopFavoritesVideoFeed()
                elif self.feedName == 'Most Responded':
                    feed = client.GetMostRespondedVideoFeed()
                elif self.feedName == 'Most Recent':
                    feed = client.GetMostRecentVideoFeed()
            self.counter = 0
            try:
                for entry in feed.entry:
                    if(entry.GetSwfUrl() is not None):
                        index = str(entry.GetSwfUrl()).index("&")
                        #28-02-2010
                        #Use Video class to store these videos
                        #Instantiate a video object
                 
                    videoObject = youtube.datastructure.Video.Video();
                    videoObject.setVideoNumber(self.counter);
                    self.counter = self.counter + 1;
                    videoObject.setThumbnails(entry.media.thumbnail[2].url)
                    self.thumbnails.append(entry.media.thumbnail[2].url)
                    videoObject.setWebPageUrl(entry.media.player.url)
                    videoObject.setTitle(entry.media.title.text)
                    videoObject.setDuration(entry.media.duration.seconds)
                    videoObject.setCategory(entry.media.category[0].text)
                    videoObject.setDate(entry.published.text[:10])
                    videoObject.setEmbedLink(entry.media.content[0].url)
                    videoObject.setSource('YouTube')
                    self.webPageUrl.append(entry.media.player.url)
                    self.videoTitle.append(entry.media.title.text)
                    self.videoDuration.append(entry.media.duration.seconds)
                    self.videoCategory.append(entry.media.category[0].text)
                    self.videoDate.append((entry.published.text[:10])) # Big String is returned we need yyyy-mm-dd
                    self.mediaLink.append(entry.media.content[0].url)
                    #put video object reference in a list
                    self.videoList.append(videoObject)
            except Exception:
                print 'Exception caught while populating youtube results'
            if self.standardFeedsActive == False:
                try:
                    metacafeCounter = self.invokeMetacafeRSSClient(self.keyword)
                except Exception:
                    print 'Metacafe Exception'
                    metacafeCounter = 0
                try:
                    truveoCounter = self.invokeTruveoRestClient(self.keyword, metacafeCounter)
                except Exception:
                    print 'Truveo Exception'
                    truveoCounter = 0
                try:
                    dailyMotionCounter = self.invokeDailyMotionRestClient(self.keyword, truveoCounter)
                except Exception:
                    print 'Daily Motion Exception'
                    dailyMotionCounter = 0
                try:
                    photBucketCounter = self.invokePhotoBucketRestClient(self.keyword, dailyMotionCounter)
                except Exception:
                    print 'Photo Bucket Exception'
                    pass
        except Exception:
            print 'Network Failure'
            pass

    def invokeMetacafeRSSClient(self, keyword):
        '''
        Calls Metacafe RSS Feed client
        '''
        metacafeClient = youtube.util.videoservice.MetacafeClient.MetacafeClient(keyword, self.counter);
        metacafeClient.restfulGet()
        metacafeClient.parse()
        
        #Added 28/02/10
        #Retrieve list of videos from Truveo
        for truveoVideo in (metacafeClient.getTruVeoVideoList()):
            
            self.videoList.append(truveoVideo)
        
        #Update parent
        return metacafeClient.getVideoCounter()
#        self.parent.callbackSearchComplete(self.videoList)
    def invokeTruveoRestClient(self, keyword, counter):
        '''
        Calls TruVeo Rest Client class
        '''
        restClient = youtube.util.videoservice.TruveoRestClient.TruveoRestClient(keyword, counter);
        restClient.restfulGet()
        restClient.parse()
        
        #Added 28/02/10
        #Retrieve list of videos from Truveo
        for truveoVideo in (restClient.getTruVeoVideoList()):
            
            self.videoList.append(truveoVideo)
        
        return restClient.getVideoCounter()

    def invokeDailyMotionRestClient(self, keyword, counter):
        '''
        Calls DailyMotion Rest Client class
        '''
        dailyMotionClient = youtube.util.videoservice.DailyMotionClient.DailyMotionClient(keyword, counter)
        dailyMotionClient.restfulGet()
        dailyMotionClient.parse()
        
        #Added 4/12/10
        #Retrieve list of videos from DailyMotion
        for truveoVideo in (dailyMotionClient.getTruVeoVideoList()):
            
            self.videoList.append(truveoVideo)
        
        return dailyMotionClient.getVideoCounter()

    def invokePhotoBucketRestClient(self, keyword, counter):
        '''
        Calls DailyMotion Rest Client class
        '''
        photoBucketClient = youtube.util.videoservice.PhotoBucketClient.PhotoBucketClient(keyword, counter)
        photoBucketClient.restfulGet()
        photoBucketClient.parse()
        
        #Added 4/12/10
        #Retrieve list of videos from DailyMotion
        for truveoVideo in (photoBucketClient.getTruVeoVideoList()):
            
            self.videoList.append(truveoVideo)
        
        return photoBucketClient.getVideoCounter()
    
#        self.appendListElements(self.thumbnails, restClient.thumbs)
##        self.thumbnails.append(restClient.thumbs);
#        self.appendListElements(self.webPageUrl, restClient.videoUrl)
##        self.webPageUrl.append(restClient.videoUrl);
#        self.appendListElements(self.videoTitle, restClient.title)
##        self.videoTitle.append(restClient.title);
#        self.appendListElements(self.videoDuration, restClient.duration)
#
##        self.videoDuration.append(restClient.duration);
#
#        self.appendListElements(self.videoCategory, restClient.category)
#
##        self.videoCategory.append(restClient.category);
#
#        self.appendListElements(self.videoDate, restClient.date)
#
##        self.videoDate.append(restClient.date);
#
#        self.appendListElements(self.mediaLink, restClient.embedUrl)
#
##        self.mediaLink.append(restClient.embedUrl);
#    def appendListElements(self,sourceList,destList):
#        for element in destList:
#            
#            
#            echo 'ss';
             
        
         
               
