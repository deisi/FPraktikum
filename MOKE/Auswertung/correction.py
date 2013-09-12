#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
''' Here the correction of the hysterese is done wich comes from diamagnetic background '''
from numpy import *
from upAndDown import upAndDown
#import matplotlib.pyplot as plt
#import pylab as py
#from scipy.optimize import minimize, leastsq, curve_fit
#from scipy.stats import chi2

# Get data
data  = genfromtxt('../Daten/Kerr Winkel/Trafo1mal30mstime.txt',delimiter=";")
dataUp, dataDo = upAndDown(data)
xDataUp, yDataUp = dataUp.T[0], dataUp.T[1]
xDataDo, yDataDo = dataDo.T[0], dataDo.T[1]

# First make a fit of the Si data than substract the function for up and down

def correctDataUp(yRealData):
    # man koente eine if abfrage für die form der Daten machen damit es immer geht ich bin zu faul denke ich
    data     = genfromtxt('../Daten/Kerr Winkel/Si10mal.txt',delimiter=";")
    dataUp   = upAndDown(data)[0]
    yDataUp  = dataUp.T[1]
    yDataCor = subtract(yRealData,yDataUp)
    #print yDataUp
    return yDataCor

print yDataUp
