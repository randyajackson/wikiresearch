import wikisearch as get
import urllib.request
import urllib.parse
import re
import pafy

wikiResults = 0
ytResults = 0


names = get.get_name_list("led zeppelin")
resultStack = []
resultStack.append(names)

for x in range(5):

    query_string = urllib.parse.urlencode({"search_query" : names[wikiResults]})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    
    while(len(search_results) == 0):
        wikiResults += 1
        
        if(names[wikiResults] > len(names) - 1):
            names = resultStack.pop()
            wikiResults = 1

        query_string = urllib.parse.urlencode({"search_query" : names[wikiResults]})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    
    url = "http://www.youtube.com/watch?v=" + search_results[0]
        

    video = pafy.new(url)
    print(url)
    print(video.keywords)
    
    check = get.get_name_list(names[wikiResults])

    if(check):
        names = get.get_name_list(names[wikiResults])
    else:
        wikiResults += 1
        names = get.get_name_list(names[wikiResults])
    
    wikiResults = 0

