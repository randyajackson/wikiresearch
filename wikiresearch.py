import wikisearch as get
import urllib.request
import urllib.parse
import re
import pafy
import collections
import wikipedia

resultStack = collections.deque()
names = get.get_name_list("jimi hendrix", resultStack)

search = ''

def ytSearch(artist):
    query_string = urllib.parse.urlencode({"search_query" : artist})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results

for x in range(5):

    search = ytSearch(resultStack.popleft())

    while(len(search[0]) == 0):
        search = ytSearch(resultStack.popleft())
    
    url = "http://www.youtube.com/watch?v=" + search[0]

    video = pafy.new(url)
    print(url)
    print(video.category)
    print(video.duration)

    get.get_name_list( resultStack.popleft() , resultStack)
    #print(resultStack)

