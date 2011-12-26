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
Created on Feb 20, 2010

@author: Rahul Sinha
'''
import gdata.youtube.service
class StandradFeedParser(object):
    '''
    classdocs
    '''
    def __init__(self, feedId):
        yt = gdata.youtube.service.YouTubeService()
        feed = yt.GetMostViewedVideoFeed()
        for entry in feed.entry:
          if(entry.GetSwfUrl() is not None):
            index = str(entry.GetSwfUrl()).index("&")
            print (entry.media.thumbnail[2].url)
            print(entry.media.player.url)
            print(entry.media.title.text)
            print(entry.media.duration.seconds)
            print(entry.media.category[0].text)
            print((entry.published.text[:10])) # Big String is returned we need yyyy-mm-dd
            print(entry.media.content[0].url)  
              
if __name__ == '__main__':
    feed = StandradFeedParser('most_viewed')
#    feed.readFeed()

    
        
