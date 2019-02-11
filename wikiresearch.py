import wikisearch as get
import urllib.request
import urllib.parse
import re
import pafy
import collections
import wikipedia



resultStack = collections.deque()
names = get.get_name_list("mf doom", resultStack)

search = ''

def ytSearch(artist):
    query_string = urllib.parse.urlencode({"search_query" : artist})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results

for x in range(5):
    print("in loop")
    search = ytSearch(resultStack.popleft())

    while(True):
        if not search:
            search = ytSearch(resultStack.popleft())
            print("no yt results")
        else:
            break
    
    url = "http://www.youtube.com/watch?v=" + search[0]

    video = pafy.new(url)

    while(video.category != "Music"):
        while(True):
            if not search:
                search = ytSearch(resultStack.popleft())
                print("not musicS")
            else:
                break
        video = pafy.new(url)

    print(url)
    print(video.category)
    print(video.duration)

    get.get_name_list( resultStack.popleft() , resultStack)
    #print(resultStack)

