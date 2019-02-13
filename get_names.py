import wikipedia
import nltk
import collections

def get_name_list(search, resultStack):	
    try:
        test = wikipedia.page(search)
        page = wikipedia.WikipediaPage(pageid = test.pageid)
        links = page.links

        names = nltk.corpus.names
        male_names = names.words('male.txt')
        female_names = names.words('female.txt')

        results = set()

        for w in links:
            first = w.split()[0]
            if(first in male_names or first in female_names or "band" in w):
                results.add(w)
                
        results = list(results)

        for x in results:
            resultStack.append(x)

        return resultStack

    except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
        resultStack.popleft()









