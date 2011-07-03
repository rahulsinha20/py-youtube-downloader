'''
Created on 04/12/2010
Daily motion client
Refer: http://home.kabelfoon.nl/~moongies/howto/mythstream_conf.html
@author: asinha
'''
import urllib2
from xml.dom.minidom import parse, parseString
import youtube.datastructure.Video
class DailyMotionClient(object):
    '''
    DailyMotion RSS Feed client
    e.g: http://www.dailymotion.com/rss/relevance/search/urmila
    '''
    def __init__(self, query, counter):
        '''
        Constructor
        '''
        
        self.counter = counter
        self.embedUrl = []
        self.title = []
        self.thumbs = []
        self.duration = []
        self.category = []
        self.date = []
        self.videoUrl = []
        self.metacafeVideoList = []
        self.query = self.convertWhiteSpacetoPerc20(query);
        self.dailyMotionRSSFeedUrl = 'http://www.dailymotion.com/rss/relevance/search/' + self.query
        
    def convertWhiteSpacetoPerc20(self, keyword):
        '''
        This method overcomes a drawback in sending a string with spaces as a query
        to Restful Veo service.
        This method checks for a blank space and converts it into %20
        e.g team india is converted as team%20india 
        '''
        parsedKeyword = '';
        for i in range(0, len(keyword)):
            #Check for a blank space
            if keyword[i] == ' ':
                #If found, replace it with %20
                parsedKeyword = parsedKeyword + '%20'
            else:
                    parsedKeyword = parsedKeyword + keyword[i];
        print 'Converted Keyword:', parsedKeyword
        return parsedKeyword
    def getVideoCounter(self):
        '''
        Returns Video Counter
        '''
        return self.counter
    def restfulGet(self):
        '''
        This models Restful Http Get
        '''
        self.RSSFeedResponse = urllib2.urlopen(self.dailyMotionRSSFeedUrl)
        self.restResponse = self.RSSFeedResponse.read()
        print 'Metacafe Response:', self.restResponse
    def parse(self):
        '''
        This method uses universal feed parser to perform XML parsing
        '''
        invalid = 'invalid'
        dom = parseString(self.restResponse);
        #Once we have a DOM Tree we should be able to access them via names
        node1 = (dom.getElementsByTagName('channel'));
#        videoSetNodes=node1[0].getElementsByTagName('VideoSet');
        #Get all videos 
        for node in node1[0].getElementsByTagName('item'):
            dailyMotionVideo = youtube.datastructure.Video.Video()
            dailyMotionVideo.setVideoNumber(self.counter);
            self.counter = self.counter + 1
            #Get titles
            try:
                
                titleList = node.getElementsByTagName('title');
                titleText = titleList[0].firstChild.data
#                print "Title:",titleText
                dailyMotionVideo.setTitle(titleText)
                self.title.append(titleText);
                
            except:
                self.title.append(invalid);
            try:
                #Get thumbnails
                #Accessing attributes refer: http://diveintopython.org/xml_processing/attributes.html
                mediaThumbsnailAttribute = node.getElementsByTagName('media:thumbnail')
                thumbsText = mediaThumbsnailAttribute[0].attributes['url'].firstChild.data
                print 'DailyMotion Thumbnail', thumbsText
                dailyMotionVideo.setThumbnails(thumbsText)
                self.thumbs.append(thumbsText)
            except:
                self.thumbs.append(invalid)
            try:
                #Get durations
                mediaDuration = node.getElementsByTagName('media:content')
                durationInSec = mediaDuration[0].attributes['duration'].firstChild.data
                print 'duration:', durationInSec
                self.duration.append(durationInSec);
                dailyMotionVideo.setDuration(durationInSec)
            except:
                self.duration.append(invalid);
            try:
                #Get Category
#                categoryList = node.getElementsByTagName('category');
#                categoryText = categoryList[0].firstChild.data;
#                print 'category:',categoryText;
                self.category.append('Daily Motion');
                dailyMotionVideo.setCategory('Daily Motion')
            except:
                self.category.append(invalid);
            try:
                #Get Date
                dateList = node.getElementsByTagName('pubDate');
                dateText = dateList[0].firstChild.data;
                print 'date:', dateText[:10];
                self.date.append(dateText[:10]);#We only need in the format YYYY-MM-DD
                dailyMotionVideo.setDate(dateText[:10])
            except:
                self.date.append(invalid)
            try:
                #Get Video URL (Not embedded)
                videoList = node.getElementsByTagName('media:player');
                videoText = videoList[0].attributes['url'].firstChild.data
                print 'video Url:', videoText;
                self.videoUrl.append(videoText);
                dailyMotionVideo.setWebPageUrl(videoText)
                #Get embed urls 
                list = node.getElementsByTagName('media:content');
                
                embedTextUrl = list[1].attributes['url'].firstChild.data
                
                self.embedUrl.append(embedTextUrl);
                print 'Embedded Url:', embedTextUrl;
                dailyMotionVideo.setEmbedLink(embedTextUrl)
            except:
                self.embedUrl.append(invalid);
            #Set the source
            dailyMotionVideo.setSource('DailyMotion')            
            #Append to the list of videos
            self.metacafeVideoList.append(dailyMotionVideo)
        
    def getTruVeoVideoList(self):
        '''
        This returns list of videos
        '''
        return self.metacafeVideoList
            
            
if __name__ == '__main__':
    keyword = 'urmila'
    parsedKeyword = ''
    for i in range(0, len(keyword)):
        print keyword[i]
        if keyword[i] == ' ':
            print 'Found Whitespace'
            parsedKeyword = parsedKeyword + '%20'
        else:
            parsedKeyword = parsedKeyword + keyword[i];
    print parsedKeyword
    obj = DailyMotionClient(parsedKeyword, 10);
    obj.restfulGet()
    obj.parse()
            
