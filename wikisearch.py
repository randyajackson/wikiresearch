import wikipedia
import nltk
from nltk.corpus import stopwords
import collections

stop = stopwords.words('english')

def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def get_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

#--------------------------------------------------------------------------------
def get_name_list(search, resultStack):
    
    try:
        test = wikipedia.page(search)
        page = wikipedia.WikipediaPage(pageid = test.pageid)
        links = page.links
        linkString = ' '.join(links)

        named_entities = get_names(linkString)

        names = set()

        for x in named_entities:
                names.add(x[0])

        list(names)

        for x in names:
            resultStack.append(x)

        return resultStack
    
    except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
        resultStack.popleft()









