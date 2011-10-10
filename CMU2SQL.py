from nltk.corpus import cmudict as cmu
import os

i = 1
for w in cmu.entries():
    print "insert into CMU.Words (ID, Word,Pronunciation) values (" + str(i) + ",'" + w[0].replace("'","''") + "','" + " ".join(w[1]) + "')"
    print "GO"
    
    #j = 1
    #for s in w[1]:
    #    print "insert into CMU.Syllables (ID,SyllableNumber,Pronunciation) values (" + str(i) + "," + str(j) + ",'" + s.replace("'","''") + "')"
    #    print "GO"
    #    j+=1
        
    i+=1