import get_names as get
import urllib.request
import urllib.parse
import re
import pafy
import youtube_dl
import collections
import wikipedia
import random

resultStack = collections.deque()
names = get.get_name_list("fleetwood mac", resultStack)

search = ''

def ensure_search(search):
    global resultStack
    search = ytSearch(resultStack.popleft())

    while not len(search):
        search = ytSearch(resultStack.popleft())
    
    return search

def ytSearch(artist):
    query_string = urllib.parse.urlencode({"search_query" : artist})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results

def get_video(search):
    try:
        search = ensure_search(resultStack.popleft())
        videoPick = random.randrange(len(search) - 1)
        url = "http://www.youtube.com/watch?v=" + search[videoPick]
        video = pafy.new(url)
    except(youtube_dl.utils.DownloadError):
        search = ensure_search(resultStack.popleft())
    
    return video

def get_length(time):
    time = time.split(":")

    timeList = []
    timeList.append(int(time[0]))
    timeList.append(int(time[1]))

    return (timeList[0] == 0 and timeList[1] < 8)

for x in range(2000):

    video = get_video(search)
    time = get_length(video.duration)

    while(True):
        if video.category == "Music" and time:
            break
        else:
            print("in music check")
            video = get_video(search)
            time = get_length(video.duration)
    
    best = video.getbestaudio()

    print(video.category)
    print(video.duration)
    print(video.keywords)
    print(best.url)

    get.get_name_list( resultStack.popleft() , resultStack)

