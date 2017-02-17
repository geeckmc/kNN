#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:16:07 2017

@author: junior
"""

from kNN import *

dataSet = createDataSet()

k = 3

point = Point(0.0, 0.0)

kNN(dataSet, k, point)