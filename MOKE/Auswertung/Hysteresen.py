#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
''' Plot the Hysterese Curves '''
import numpy as np
import matplotlib.pyplot as plt
import pylab as py
from scipy.optimize import minimize, leastsq, curve_fit
from scipy.stats import chi2

# Get data Up
data  = np.genfromtxt('../Daten/Kerr Winkel/Haesler10mal30ms.txt',delimiter=";")
xData = data.T[0]
yData = data.T[1]
yerr  = 5*np.ones(len(xData))
print data
