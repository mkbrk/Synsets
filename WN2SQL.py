from nltk.corpus import wordnet as wn
import os

for s in wn.all_synsets():
    print "insert into WN.Synsets (ID,Definition,POS) values ('" + s.name + "','" + s.definition.replace("'","''") + "','" + s.pos + "')"
    print "GO"
    
    for l in s.lemmas:
        print "insert into WN.Lemmas (ID,Lemma) values ('" + s.name + "','" + l.name.replace("'","''").replace("_", " ") + "')"
        print "GO"
        for a in l.antonyms():
            print "insert into WN.Antonyms (ID,Lemma,AntonymID,AntonymLemma) values ('" + s.name + "','" + l.name.replace("'","''").replace("_", " ") + "','" + a.synset.name + "','" + a.name.replace("'","''").replace("_"," ") + "')"
            print "GO"
            
    
    for e in s.examples:
        print "insert into WN.Examples (ID,Example) values ('" + s.name + "','" + e.replace("'","''") + "')"
        print "GO"
        
    for h in s.hypernyms():
        print "insert into WN.Hypernyms (ID,HypernymID) values ('" + s.name + "','" + h.name + "')"
        print "GO"
    
