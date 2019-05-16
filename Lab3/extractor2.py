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
    content = re.sub("\[.*\]", "", content)
    content = re.sub("'s", " name", content)
    tokens = nltk.word_tokenize(content)
    t = nltk.pos_tag(tokens)
    for ti in t:
        if ti[1] in ["VB", "VBP", "VBZ", "VBD"]:
            exp = "^[^&].*? " + ti[0] + " "
            # print(ti[0])
            # print(exp)
            content = re.sub(exp, "", content)
            # print(content)
            break
    print (t)

    tokens1 = nltk.word_tokenize(content)
    t1 = nltk.pos_tag(tokens1)
    # print(t1)


    grammar = r"""
        NP: {(<DT>|<CD>)?(<JJ>|<NNP>|<NN>|<NNS>|<POS>|JJS|JJR)*(<NN>|<NNS>)+}
        	{(<DT>|<CD>)<JJ>*<VBG>*(<NN>|<NNS>)+}
        	{(<DT>|<CD>)<NNP>+}
    """
    cp = nltk.RegexpParser(grammar)
    tree = cp.parse(t1)
    # tree.draw()
          
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            print(subtree)
            leaf = subtree.leaves()
            if leaf[len(leaf)-1][0] in ["sort", "kind", "type", "number","name", "kinds", "range", "body", "word", "style", "forms", "set"]:
                continue
            elif leaf[len(leaf)-1][0] in ["term", "part"]:
                if len(leaf)<=2:
                    continue
                else:
                    return leaf[len(leaf)-2][0]
            elif leaf[len(leaf)-1][1] == "NNP": 
                key = leaf[0][0]
                for i in range(1, len(leaf)):
                    key = key+ " "+ leaf[i][0]
                print(key)
                return key
            else:
                print(leaf[len(leaf)-1][0])
                return leaf[len(leaf)-1][0]
            # print(subtree.leaves())
            # for i in range():
            # 	if leaf[1] == ""
            # 	print(leaf[0])
            # break
    # hfcbgj

    return None

with open(sys.argv[2], 'w', encoding="utf-8") as output:
    index = 0
    for page in Parser(sys.argv[1]):
        index += 1
        # if index == 5:
        typ = extractType(page.content)
        if typ:
            output.write(page.title + "\t" + typ + "\n")
        if index == 3:
            break

