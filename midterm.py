#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:26:36 2019

@author: markasuncion
"""

def mylog(x,b):
    count = 0
    curr = b
    while curr <= x:
        curr *= b
        count += 1
    return count

def getSublists(L,n):
    x = len(L)
    sub = []
    list_of_sub = []
    for i in range(x - 1):
        for j in range(n - 1):
            sub.append(L[j])
        list_of_sub.append(sub)
    return list_of_sub
        
        
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    result = []
    for item in aDict:
        if aDict[item] == target:
            result.append(item)
    return result

def laceStringsRecur(s1, s2):

    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out+s2 #Edge case checks 
        if s2 == '':
            return out+s1
        else:
            return helpLaceStrings(s1[1 :], s2[1 :], out+s1[0]+s2[0])
    return helpLaceStrings(s1, s2, '')