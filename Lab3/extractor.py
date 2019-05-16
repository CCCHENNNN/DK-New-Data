'''Extracts type facts from a wikipedia file
usage: extractor.py wikipedia.txt output.txt

Every line of output.txt contains a fact of the form
    <title> TAB <type>
where <title> is the title of the Wikipedia page, and
<type> is a simple noun (excluding abstract types like
sort, kind, part, form, type, number, ...).

If you do not know the type of an entity, skip the article.
(Public skeleton code)'''

from parser import Parser
import sys
import re
import nltk

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(-1)

def extractType(content):
    # Code goes here
    # Deal with the content, cut the symbols "[" "]" in the content
    content = re.sub("[][]+", " ",content)
    # Cut the abstract type words like "sort, kind, part, form, type, number..." 
    # in order to avoid being disturbed by them 
    content = re.sub(" form of|type of|style of|part of|sort of|kind of|one of|set of|forms of|body of|word for|range of|number of|used to", "",content)
    content = re.sub("'s", " name",content) # because sometimes nltk has the error tag for "'s", so I change into a noun

    noun = [] # list to record the leaves of NP
    # analyze the content
    words = nltk.word_tokenize(content)
    pos_tags = nltk.pos_tag(words)
    vb = "" # the verb word who appears in the content
    # print(pos_tags)

    # cut the words from the beginning to the first verb word
    rep = ""
    has_vb = 0
    # when the first word of the content is verb
    if pos_tags[0][1] in ["VBZ","VB","VBD","VBG","VBN","VBP"]:
        has_vb = 1
        rep = pos_tags[0][0]
        content = re.sub(rep,"",content)
    # when the first word of the content is not verb
    else:
        for word,pos in pos_tags:
            if pos in ["VBZ","VB","VBD","VBG","VBN","VBP"]:
                has_vb = 1
                vb = word
                break
        rep = "^[^&].*? " + vb + " "
        if vb != "":
            content = re.sub(rep,"",content)

    # print(content)

    # using nltk to reanalyze the new content with tags
    words = nltk.word_tokenize(content)
    pos_tags = nltk.pos_tag(words)

    # NP is the regular expression of a complet noun such like "a pretty girl"
    grammer = 'NP:{<CD>*<DT>*<NNP|NN|NNPS|JJ|JJR|JJS|RBS|VBN|VBG|POS>*<RP>*<NN|NNS|NNP>+<VB>*}'
    cp = nltk.RegexpParser(grammer)
    tree = cp.parse(pos_tags) # the grammer tree of this content
    # print(tree)
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            noun.append(subtree.leaves())
    # print(noun)

    result = ""
    # if the content has no verb, taking the first noun into the result
    # if the content has verb, taking the first noun after the verb into the result
    if len(noun) > 0:
        if has_vb == 0 and len(noun) > 1:
            return noun[1][-1][0]
        else:
            if noun[0][0][0] == pos_tags[0][0]: # the first word after verb should be same as that in first NP
                return noun[0][-1][0]

    return result

with open(sys.argv[2], 'w', encoding="utf-8") as output:
    for page in Parser(sys.argv[1]):
        typ = extractType(page.content)
        if typ:
            output.write(page.title + "\t" + typ + "\n")

