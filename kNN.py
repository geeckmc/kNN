# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from numpy import *
from math import *

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __to_string__(self):
        print(" ( {0}, {1} ) ".format(self.x, self.y))

def createDataSet():
    dataSet = {}
    dataSet[Point(1.0, 1.1)] = 'A'
    dataSet[Point(1.0, 1.0)] = 'A'
    dataSet[Point(0.0, 0.0)] = 'B'
    dataSet[Point(0.0, 0.1)] = 'B'
    # Add another point
    return dataSet
    
def distance(current, point):
    return math.sqrt( math.pow((current.x - point.x), 2) + math.pow((current.y - point.y), 2) )
    

dico = createDataSet()

point = Point(0.0, 0.0)

var = []

for pt,label in dico.items():
    temp = [distance(point, pt), label]
    var.append(temp)

def order(res):
    #Tri à bulles
    n=len(res)
    for i in reversed(range(1, n+1)):
        for j in range(2, i+1):
            if(res[j-2][0]>res[j-1][0]):
                temp = res[j-1]
                res[j-1] = res[j-2]
                res[j-2] = temp
    return res
        

def choix(liste, k):
    countA=0
    countB=0
    for i in range(3):
        if(liste[i][1]=='A'):
            countA += 1
        else:
            countB += 1
    if(countA>=countB):
        print('A')
    else:
        print('B')
            

def kNN(dataSet, k, toClassify):
    var = []

    for pt,label in dataSet.items():
        temp = [distance(toClassify, pt), label]
        var.append(temp)
    choix(order(var),k)
    
    