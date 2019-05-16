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
        title = ""

        # cut the prefix and postfix of the title
        if page.title[-3] == '_':
          title = page.title.strip()[1:-3].replace("_"," ")
        else:
          title = page.title.strip()[1:-4].replace("_"," ")

        # remove the symbols of the content
        content = page.content.strip()
        content = re.sub("[\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",content)

        # The idea of disambiguation is that:
        # 1. From the title, we can get the number of the potential number of ontologies
        # 2. Then for each ontology, we find the link ontologies
        # 3. Get the labels of the link ontologies
        # 4. Match the labels with the content that we want to disambiguate
        # 5. Vote for the final ontology

        # Get the potential number of ontologies
        reverse_ont = wikidata.rlabels.get(title)
        ont_set = {} #to record the matched word number of each ontology
        tmp =[]
        for ont in reverse_ont:
          count = set() #to record the matched word for this ontology from the link ontology
          link_onts = wikidata.links.get(ont)
          for link_ont in link_onts:
            link_labels = wikidata.labels.get(link_ont)

            # check for the information of the date, but the result is not better
            # if len(wikidata.dates) > 0:
            #   link_dates = wikidata.dates.get(link_ont)
            #   if str(link_dates) != "None":
            #     for link_date in link_dates:
            #       link_date_div = str(link_date).replace("#","").replace("-"," ").split()
            #       months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            #       if len(link_date_div) == 1:
            #         if content.find(" " + link_date_div[0] + " ") >= 0:
            #           count.add(link_date_div[0])
            #       elif len(link_date_div) == 3:
            #         if content.find(" " + link_date_div[0] + " ") >= 0:
            #           count.add(link_date_div[0])
            #         elif content.find(" " + link_date_div[2] + " ") >= 0:
            #           count.add(link_date_div[2])
            #         elif content.find(months[int(link_date_div[1]) - 1]) >= 0:
            #           count.add(months[int(link_date_div[1]) - 1])


            # check the information of the other words
            for link_label in link_labels:
              # the set of tags which are useless for disambiguation
              tags = set(['the', 'of',  'at', 'for', 'down', 'in', 'from',  'with', 'by', 'on', 'about',  'de', 'if', 'a', 'upon',  'an',   'every', 'this',  'into',  'as', 'out',  'during',   'some',  'en',  'von', 'all',  'since', 'Bout',  'after', 'after',  'under', 'below',  'over', 'those',  'behind', 'per', 'during', 'no',  'like', 'these',   'within',   'against',  'up',  'upper',  'near', 'without', 'before', 'beyond', 'outside','of','and','is','to'])
              words = link_label.split()

              # split all label to verify if it matches the words of content
              for word in words:
                word = word.replace(",","").replace("(","").replace(")","").lower()
                if word not in tags: 
                  if word.endswith('es'):
                      if (content.lower().find(word.rstrip('es')) >= 0):
                          count.add(word)
                  elif word.endswith('s'):
                      if (content.lower().find(word.rstrip('s')) >= 0):
                          count.add(word)
                  else:
                      if (content.lower().find(word) >= 0):
                          count.add(word) 
          if len(count) > 0:
            ont_set[ont] = len(count) #record the number of matched word

        
        # calculate the score of each linked ontology
        nbs = []
        for ont in ont_set:
          nbs.append(ont_set[ont])
        maxs = heapq.nlargest(2, nbs)
        if len(maxs) >= 2 and maxs[0] - maxs[1] <= 2:
          for ont in ont_set:
            ont_set[ont] = ont_set[ont]/len(wikidata.links[ont])

        # find the ontology who has the highest score of the set and determine it for the final ontology
        max_ont = ""
        max_nb = 0
        for ont in ont_set:
          if ont_set[ont] > max_nb:
            max_nb = ont_set[ont]
            max_ont = ont
        if max_ont == "":
          for ont in wikidata.rlabels.get(title):
            max_ont = ont
            break
        print(page.title, max_ont, sep="\t", file=output)
        pass
