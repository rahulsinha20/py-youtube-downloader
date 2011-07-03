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

    
        
