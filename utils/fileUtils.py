# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:08:41 2016

@author: jgarrison
"""

def getLineCount(fileName):
    totalInFile = 0
    with open(fileName, 'r', encoding="utf8") as fIn:        
        for line in iter(fIn):
           totalInFile = totalInFile + 1
        fIn.close()
    return totalInFile

