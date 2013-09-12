#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
'''background substitutes the Diamagnetic background from given Data'''

from numpy import *
import matplotlib.pyplot as plt
from hystFit import hystFitUp, hystFitDo, hystFit
from upAndDown import upAndDown
from kalibration import calUpI, calDoI
#import pylab as py
#from scipy.optimize import minimize, leastsq, curve_fit
#from scipy.stats import chi2
#testData = genfromtxt('../Daten/Kerr Winkel/Trafo10mal.txt', delimiter=';')

def background(z):
    zUp , zDo = upAndDown(z)
    # Get data
    data  = genfromtxt('../Daten/Kerr Winkel/Si10mal.txt', delimiter=';')
    dataUp, dataDo = upAndDown(data)

    # make the backgound Fit
    #fit   = hystFit(dataUp)
    fitUp = hystFit(dataUp) # in V
    fitDo = hystFit(dataDo) # in V
    def fitUpN(z): return fitUp(z)*1000 # in mV
    def fitDoN(z): return fitDo(z)*1000 # in mV

    resultUp = zUp - fitUp(zUp)
    resultDo = zUp - fitUp(zDo)

    return append(resultUp, resultDo, axis=0)
