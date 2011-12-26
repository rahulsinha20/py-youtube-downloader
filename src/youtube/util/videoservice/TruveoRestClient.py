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
Created on Feb 24, 2010

@author: Rahul Sinha
'''
import urllib2 
import string
from xml.dom.minidom import parse, parseString
import youtube.datastructure.Video
class TruveoRestClient(object):
    '''
    Truveo REST Client implementation
    e.g: http://xml.truveo.com/apiv3?appid=1x1jhj64466mi12ia&method=truveo.videos.getVideos&query=urmila&results=50
    '''


    def __init__(self, query, counter):
        '''
        Constructor
        '''
        self.baseUrl = 'http://xml.truveo.com/apiv3';
        self.appId = '1x1jhj64466mi12ia';
        self.method = 'truveo.videos.getVideos';
        self.query = self.convertWhiteSpacetoPerc20(query);
        self.restfulUrl = self.baseUrl + '?appid=' + self.appId + '&method=' + self.method + "&query=" + self.query + "&results=50";
        print 'TruVeo Restful service Url:', self.restfulUrl;
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
        node1 = (dom.getElementsByTagName('Response'));
        videoSetNodes = node1[0].getElementsByTagName('VideoSet');
        #Get all videos 
        for node in videoSetNodes[0].getElementsByTagName('Video'):
            trueveoVideo = youtube.datastructure.Video.Video()
            trueveoVideo.setVideoNumber(self.counter);
            self.counter = self.counter + 1
            #Get titles
            try:
                
                titleList = node.getElementsByTagName('title');
                titleText = titleList[0].firstChild.data
                print "Title:", titleText
                trueveoVideo.setTitle(titleText)
                self.title.append(titleText);
                
            except:
                self.title.append(invalid);
            try:
                #Get thumbnails
                thumbsList = node.getElementsByTagName('thumbnailUrl');
                thumbstext = thumbsList[0].firstChild.data;
                print 'Thumbail:', thumbstext
                trueveoVideo.setThumbnails(thumbstext)
                self.thumbs.append(thumbstext);
            except:
                self.thumbs.append(invalid);
            try:
                #Get durations
                durationList = node.getElementsByTagName('runtime');
                durationText = durationList[0].firstChild.data;
                print 'Duration:', durationText;
                self.duration.append(durationText);
                trueveoVideo.setDuration(durationText)
            except:
                self.duration.append(invalid);
            try:
                #Get Category
                categoryList = node.getElementsByTagName('category');
                categoryText = categoryList[0].firstChild.data;
                print 'category:', categoryText;
                self.category.append(categoryText);
                trueveoVideo.setCategory(categoryText)
            except:
                self.category.append(invalid);
            try:
                #Get Date
                dateList = node.getElementsByTagName('dateProduced');
                dateText = dateList[0].firstChild.data;
                print 'date:', dateText[:10];
                self.date.append(dateText[:10]);#We only need in the format YYYY-MM-DD
                trueveoVideo.setDate(dateText[:10])
            except:
                self.date.append(invalid)
            try:
                #Get Video URL (Not embedded)
                #check if the channel is from youtube
                channelName = node.getElementsByTagName('channel');
                if channelName[0].firstChild.data == 'YouTube':
                    #for e.g <videoPlayerEmbedTag><object width="425" height="344"><param name="movie" value="http://www.youtube.com/v/t_97FH0uqO4"></param><param name="allowFullScreen" value="true"></param><embed flashvars="fs=1" allowfullscreen="true" src="http://xml.truveo.com/eb/i/2690112902/a/70a7dc249f1af3e321b3e0e9402c6b65/p/50/h/4cfa05ab4827950:137306da83afae3694f2ec0925bed7c0" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed></object></videoPlayerEmbedTag>
                    #Extract video url as the youtube link
                    youTubeEmbedLink = node.getElementsByTagName('videoPlayerEmbedTag');
                    youTubeEmbedLinkText = youTubeEmbedLink[0].firstChild.data
                    beginIndex = youTubeEmbedLinkText.find('value=')
                    uTubeText = youTubeEmbedLinkText[beginIndex + len('value=') + 1:]
                    endIndex = uTubeText.find('">')
                    finalUTubeLink = uTubeText[:endIndex]
                    print 'Found YouTube Link:', finalUTubeLink
                    self.videoUrl.append(finalUTubeLink);
                    trueveoVideo.setWebPageUrl(finalUTubeLink)
                else:    
                    videoList = node.getElementsByTagName('videoUrl');
                    videoText = videoList[0].firstChild.data;
                    print 'video Url:', videoText;
                    self.videoUrl.append(videoText);
                    trueveoVideo.setWebPageUrl(videoText)
                #Get embed urls 
                list = node.getElementsByTagName('videoPlayerEmbedTag');
                
                embedText = list[0].firstChild.data
                beginIndex = embedText.find('src=');
                temptext = embedText[beginIndex + len('src=') + 1:]
                    
                endIndex = temptext.find('"');
                embedTextUrl = temptext[:endIndex];
                self.embedUrl.append(embedTextUrl);
                print 'Embedded Url:', embedTextUrl;
                trueveoVideo.setEmbedLink(embedTextUrl)
            except:
                self.embedUrl.append(invalid);
#           #Set the source
            trueveoVideo.setSource('Trueveo')            
            #Append to the list of videos
            self.trueVeoVideoList.append(trueveoVideo)
        
    def getTruVeoVideoList(self):
        '''
        This returns list of videos
        '''
        return self.trueVeoVideoList
            
            
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
    obj = TruveoRestClient(parsedKeyword, 10);
    obj.restfulGet()
    obj.parse()
    
        
        
        
