import wikipedia
from nltk.tag import StanfordNERTagger


def get_continuous_chunks(tagged_sent):
    continuous_chunk = []
    current_chunk = []

    for token, tag in tagged_sent:
        if tag != "O":
            current_chunk.append((token, tag))
        else:
            if current_chunk: # if the current chunk is not empty
                continuous_chunk.append(current_chunk)
                current_chunk = []
    # Flush the final current_chunk into the continuous_chunk, if any.
    if current_chunk:
        continuous_chunk.append(current_chunk)
    return continuous_chunk

#--------------------------------------------------------------------------------

test = wikipedia.page("Os Mutantes")
page = wikipedia.WikipediaPage(pageid = test.pageid)
links = page.links

jar = '/var/www/randyjackson.net/public_html/research/wikiresearch/nert/stanford-ner-2018-10-16/stanford-ner.jar'
model = '/var/www/randyjackson.net/public_html/research/wikiresearch/nert/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz'

stner = StanfordNERTagger(model, jar, encoding='utf8')
tagged_sent = stner.tag(links)

named_entities = get_continuous_chunks(tagged_sent)
named_entities_str_tag = [(" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]

names = set()

#for x in named_entities_str_tag:
    #if(x[1] == 'PERSON'):
        #names.add(x[0])

print(named_entities_str_tag)









