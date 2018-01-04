# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:00:34 2017

@author: jgarrison
"""
from nltk.corpus import stopwords
import string

cachedStopWords = stopwords.words("english")

class NLPString:
    
    def __init__(self):
        self.blah = ""
    
    def RemoveStopWordsAndPunctuation(text):
    
        textWithOutStopWords = ' '.join([word for word in text.split() if word not in cachedStopWords])
        
        punctuations = list(string.punctuation)
        punctuations.append("“")
        punctuations.append("”")
    
        textWithOutPunctuations = " ".join("".join([" " if ch in punctuations else ch for ch in textWithOutStopWords]).split())
       
        return textWithOutPunctuations.lower()
