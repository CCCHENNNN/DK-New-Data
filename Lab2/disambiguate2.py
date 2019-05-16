usage='''
  Given as command line arguments
  (1) wikidataLinks.tsv 
  (2) wikidataLabels.tsv
  (optional 2') wikidataDates.tsv
  (3) wikipedia-ambiguous.txt
  (4) the output filename'''
'''writes lines of the form
        title TAB entity
  where <title> is the title of the ambiguous
  Wikipedia article, and <entity> is the 
  wikidata entity that this article belongs to. 
  It is OK to skip articles (do not output
  anything in that case). 
  (Public skeleton code)'''

import sys
import re
import operator
import heapq
from parser import Parser
from simpleKB import SimpleKB

if __name__ == "__main__":
    if len(sys.argv) is 5:
        dateFile = None
        wikipediaFile = sys.argv[3]
        outputFile = sys.argv[4]
    elif len(sys.argv) is 6:
        dateFile = sys.argv[3]
        wikipediaFile = sys.argv[4]
        outputFile = sys.argv[5]
    else:
        print(usage, file=sys.stderr)
        sys.exit(1)

    wikidata = SimpleKB(sys.argv[1], sys.argv[2], dateFile)
# wikidata is here an object containing 4 dictionaries:
## wikidata.links is a dictionary of type: entity -> set(entity).
##                It represents all the entities connected to a
##                given entity in the yago graph
## wikidata.labels is a dictionary of type: entity -> set(label).
##                It represents all the labels an entity can have.
## wikidata.rlabels is a dictionary of type: label -> set(entity).
##                It represents all the entities sharing a same label.
## wikidata.dates is a dictionnary of type: entity -> set(date).
##                It represents all the dates associated to an entity.

# Note that the class Page has a method Page.label(),
# which retrieves the human-readable label of the title of an 
# ambiguous Wikipedia page.

with open(outputFile, 'w', encoding="utf-8") as output:
    for page in Parser(wikipediaFile):
        # DO NOT MODIFY THE CODE ABOVE THIS POINT
        # or you may not be evaluated (you can add imports).
        
        # YOUR CODE GOES HERE:
        
        # The main idea:
        # For each page, we have several entities with the same label as its
        # To get the contexts of each entity, to record the number of words same as the content of page
        # So, for each page, there is a list of number of words and a dictionary (key=entity, value=?)
        # To get the two maximum values, x and y, if x-y>=2, the value of dictionary for the key entity is just the maximum number of words
        # if x-y<2, the value of dictionary for the key entity is number of words divide the size of number of links for the entity.
    
        # count is a dictionary: to remember the score for each entity related by the label of page.
        count = {}
        
        #tmp is a list: to remember the number of words corresponding to the page content for each entity with the same lable as the page
        tmp =[]
        content = page.content.lower()


        for e in wikidata.rlabels[page.label()]:
            cnt = set()
            links = wikidata.links[e]
            #links is a set: a set of entity to which entity e has links.
            
            for link in links:
                
                #labels is a set: a set of labels of each linked entity
                labels = wikidata.labels[link]
                
                for label in labels:
                   
                    #compare each word in the label with page.content
                    for w in re.split(r"\s|,\s|\s\(|\)", label):
                        w1 = w.lower()
                        if w1 != None:
                            #filter out some useless words
                            if w1 not in ["and","is","of", "the", "from", "in", "at", "on", "by","a", "an", "with", "to", "for", "about", "after", "since", "as", "de"]:
                                #handle some plural words
                                if w.endswith('ies'):
                                    if (content.find(w1.rstrip('ies'))!=-1):
                                        cnt.add(w1) 
                                elif w.endswith('es'):
                                    if (content.find(w1.rstrip('es'))!=-1):
                                        cnt.add(w1)
                                elif w.endswith('s'):
                                    if (content.find(w1.rstrip('s'))!=-1):
                                        cnt.add(w1)
                                else:
                                    if (content.find(w1) != -1):
                                        cnt.add(w1)                         
                   
            tmp.append(len(cnt))
        #max2 is a list: get the two largest number of words for each entity
        max2 = heapq.nlargest(2, tmp)
        
        # if max2[0]-max2[1]>=2, it means that there are relative long distances for the two entities, 
        # so I can just get the entity who has a largest number of words
        # else, it means that the distance between the two entities id=s not so far, 
        # so I need to make a calculation: 
        # number of words same as the content of page divide number of links for the entity
        # this a relative value to compare two entity, which one is more closer to the page
        
        if len(max2)>= 2:
            if max2[0]-max2[1]>=2:
                i = 0
                for e in wikidata.rlabels[page.label()]:
                    count[e] = tmp[i]
                    i += 1
            else:
                j = 0
                for e in wikidata.rlabels[page.label()]:
                    count[e] = tmp[j]/len(wikidata.links[e])
                    j += 1
        else:
            j = 0
            for e in wikidata.rlabels[page.label()]:
                count[e] = tmp[j]/len(wikidata.links[e])
                j += 1
        ee = max(count.items(), key=operator.itemgetter(1))[0]
     
        print(page.title, ee, sep='\t', file=output)
       
        pass
