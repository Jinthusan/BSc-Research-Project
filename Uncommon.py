#!/usr/bin/env python
# coding: utf-8

# In[51]:


import nltk
from nltk.tokenize import word_tokenize
import string

def runUncommon():
    s = open(r"C:\Users\JINTHUSAN\AppData\Roaming\nltk_data\corpora\state_union\sample_poem.txt")
    a = []
    for word in word_tokenize(s.read()):
        # print(word)
        a.append(word)
        a = [word for word in a if word.isalpha()]
        totalwordcount = len(a)
    print(a)
    print(totalwordcount)

    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/', None)
    data = {'TotalWordCount': totalwordcount}

    result = firebase.patch('/cdapresearchtest-9bd7c/WordCount/TotCount', data)

    # In[52]:

    # d = open(r"C:\Users\JINTHUSAN\AppData\Roaming\nltk_data\corpora\state_union\output.txt")
    d = "I am Happy"
    b = []
    for word in word_tokenize(d):
        # print(word)
        b.append(word)
    print(b)

    # In[53]:

    def uncommon(s, d):


        uc = ''
        for i in s:
            if i not in d:
                uc = uc + " " + i
        for j in d:
            if j not in s:
                uc = uc + " " + j

        return uc

    print("Uncommon words are :", uncommon(a, b))

    # In[54]:

    num = uncommon(a, b).count(" ")
    print('Number of missing words :', num)

    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://cdapresearchtest-9bd7c.firebaseio.com/',None)
    data = {'MissingCount': num }

    result = firebase.patch('/cdapresearchtest-9bd7c/Missing/count', data)

    # In[ ]:
runUncommon()


