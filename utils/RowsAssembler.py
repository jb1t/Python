# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:25:53 2017

@author: jgarrison
"""
import json

def ConvertFetchAllToArrayOfDict(cursor):
    
    columns = [column[0] for column in cursor.description]
    
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    
    return results

def ConvertRowsToArrayOfDictWithCustomColumns(columnNames, rows):
    results = []
    for row in rows:
        results.append(dict(zip(columnNames, row)))
    
    return results

def ConvertRowsToArrayOfDict(cursorDescription, rows):
    
    columns = [column[0] for column in cursorDescription]
    
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    
    return results

def ConvertRowsToJson(cursorDescription, rows):
    columns = [column[0] for column in cursorDescription]
    
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    
    return json.dumps(results)
