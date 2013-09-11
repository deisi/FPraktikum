#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
from numpy import *
from upAndDown import upAndDown
#import matplotlib.pyplot as plt
#import pylab as py
#from scipy.optimize import minimize, leastsq, curve_fit
#from scipy.stats import chi2

# Get data
data  = genfromtxt('../Daten/Kerr Winkel/Si10mal.txt',delimiter=";")
xData = data.T[0]
yData = data.T[1]

def correctDataUp(yRealData):
    data     = genfromtxt('../Daten/Kerr Winkel/Si10mal.txt',delimiter=";")
    dataUp   = upAndDown(data)[0]
    yDataUp  = dataUp.T[1]
    yDataCor = subtract(yRealData,yDataUp)
    #print yDataUp
    return yDataCor

print correctDataUp(yData)
