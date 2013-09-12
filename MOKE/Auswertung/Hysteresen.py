#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
''' Plot the Hysterese Curves '''
from kalibration import calUpI, calDoI
from upAndDown import upAndDown
from numpy import *
import matplotlib.pyplot as plt
import pylab as py
from scipy.optimize import minimize, leastsq, curve_fit
from scipy.stats import chi2

# Get data
data  = genfromtxt('../Daten/Kerr Winkel/Si10mal.txt',delimiter=";")
#yerr  = 5*np.ones(len(xData))
dataUp, dataDo = upAndDown(data)
xDataUp, yDataUp = dataUp.T[0], dataUp.T[1]
xDataDo, yDataDo = dataDo.T[0], dataDo.T[1]


plt.figure() 
#plt.subplot(211) 
plt.title(r'Ein vielsagender Titel')
plt.plot(calUpI(xDataUp), yDataUp, 'x', label= r'Up', color='r') 
plt.plot(calDoI(xDataDo), yDataDo, 'x', label= r'Down', color='g') 
#plt.xlabel(r'Strom I in $[A]$')
plt.xlabel(r'Mag. Feld B in $[mT]$') 
leg = plt.legend(loc='best', fancybox=True)   # Durchsichtige Legend sehr geil 
leg.get_frame().set_alpha(0.5) 
#plt.savefig('PrettyPlot.png') 
plt.show()

