'''
Created on 03/12/2010

@author: asinha
'''

import urllib2 
import string
from xml.dom.minidom import parse, parseString
import youtube.datastructure.Video
class GoogleVideoClient(object):
    '''
    Google Video Client implementation
    e.g http://video.google.com/videofeed?type=search&num=20&output=rss&q=mashup
    '''


    def __init__(self, query, counter):
        '''
        Constructor
        '''
        self.baseUrl = 'http://video.google.com/videofeed?type=search&num=20&output=rss&q='
        self.query = self.convertWhiteSpacetoPerc20(query);
        self.restfulUrl = self.baseUrl + self.query
        print 'Google Video RSS Feeds Url:', self.restfulUrl;
        self.embedUrl = [];
        self.title = [];
        self.thumbs = [];
        self.duration = [];
        self.category = [];
        self.date = [];
        self.videoUrl = [];
        self.trueVeoVideoList = []
        self.counter = counter

    def getVideoCounter(self):
        '''
        Returns Video Counter
        '''
        return self.counter        
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

    def restfulGet(self):
        '''
        This models Restful Http Get
        '''
        self.restResponseStream = urllib2.urlopen(self.restfulUrl);
        self.restResponse = self.restResponseStream.read();
        print 'Response:', self.restResponse
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
            #Check if we have an embedded google player, if not skip
            #Get embed urls 
            list = node.getElementsByTagName('media:content');
            embedTextUrl = list[0].attributes['url'].firstChild.data                
            self.embedUrl.append(embedTextUrl);
#            print 'Embedded Url:',embedTextUrl;
            if embedTextUrl.find('googleplayer.swf') == -1:
                print 'nothing'
            else:
                googleVideo = youtube.datastructure.Video.Video()
                googleVideo.setVideoNumber(self.counter);
                self.counter = self.counter + 1
                googleVideo.setEmbedLink(embedTextUrl)
                print 'Embed Link:', embedTextUrl
                #Get titles
                try:
                    
                    titleList = node.getElementsByTagName('title');
                    titleText = titleList[0].firstChild.data
    #                print "Title:",titleText
                    googleVideo.setTitle(titleText)
                    self.title.append(titleText);
                    
                except:
                    self.title.append(invalid);
                try:
                    #Get thumbnails
                    #Accessing attributes refer: http://diveintopython.org/xml_processing/attributes.html
                    mediaThumbsnailAttribute = node.getElementsByTagName('media:thumbnail')
                    thumbsText = mediaThumbsnailAttribute[0].attributes['url'].firstChild.data
                    print 'Google Thumbnail', thumbsText
                    googleVideo.setThumbnails(thumbsText)
                    self.thumbs.append(thumbsText)
                except:
                    self.thumbs.append(invalid)
                try:
                    #Get durations
    #                durationList = node.getElementsByTagName('runtime');
    #                durationText = durationList[0].firstChild.data;
    #                print 'Duration:',durationText;
                    durationText = '10'
                    self.duration.append(durationText);
                    googleVideo.setDuration(durationText)
                except:
                    self.duration.append(invalid);
                try:
                    #Get Category
                    categoryList = node.getElementsByTagName('category');
                    categoryText = categoryList[0].firstChild.data;
                    print 'category:', categoryText;
                    self.category.append('Google Video');
                    googleVideo.setCategory(categoryText)
                except:
                    self.category.append(invalid);
                try:
                    #Get Date
                    dateList = node.getElementsByTagName('pubDate');
                    dateText = dateList[0].firstChild.data;
                    print 'date:', dateText[:10];
                    self.date.append(dateText[:10]);#We only need in the format YYYY-MM-DD
                    googleVideo.setDate(dateText[:10])
                except:
                    self.date.append(invalid)
                try:
                    #Get Video URL (Not embedded)
                    videoList = node.getElementsByTagName('media:player');
                    videoText = videoList[0].attributes['url'].firstChild.data
                    print 'video Url:', videoText;
                    self.videoUrl.append(videoText);
                    googleVideo.setWebPageUrl(videoText)
                    
                except:
                    self.embedUrl.append(invalid);
    #            
                #Append to the list of videos
                self.metacafeVideoList.append(googleVideo)
        
    def getTruVeoVideoList(self):
        '''
        This returns list of videos
        '''
        return self.trueVeoVideoList
            
            
if __name__ == '__main__':
    keyword = 'mashup'
    parsedKeyword = ''
    for i in range(0, len(keyword)):
        print keyword[i]
        if keyword[i] == ' ':
            print 'Found Whitespace'
            parsedKeyword = parsedKeyword + '%20'
        else:
            parsedKeyword = parsedKeyword + keyword[i];
    print parsedKeyword
    obj = GoogleVideoClient(parsedKeyword, 10);
    obj.restfulGet()
    try:
        obj.parse()
    except Exception:
        pass
    
        
        
        
