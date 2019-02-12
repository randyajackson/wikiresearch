import get_names as get
import urllib.request
import urllib.parse
import re
import pafy
import collections
import wikipedia

resultStack = collections.deque()
names = get.get_name_list("tiny moving parts", resultStack)

search = ''
def ensure_search(search):
    global resultStack
    search = ytSearch(resultStack.popleft())

    while not len(search):
        search = ytSearch(resultStack.popleft())
        print("no yt results")
    
    return search

def ytSearch(artist):
    query_string = urllib.parse.urlencode({"search_query" : artist})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results

for x in range(5):
    search = ensure_search(resultStack.popleft())
    url = "http://www.youtube.com/watch?v=" + search[0]
    video = pafy.new(url)

    while(video.category != "Music"):
        print("in music check")
        search = ensure_search(resultStack.popleft())

        url = "http://www.youtube.com/watch?v=" + search[0]
        video = pafy.new(url)


    print(url)
    print(video.category)
    print(video.duration)
    print(video.keywords)

    get.get_name_list( resultStack.popleft() , resultStack)

