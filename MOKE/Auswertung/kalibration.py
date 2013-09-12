#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
'''
These Functions make up the kalibration for getting from I in [A] to B in [mT] and V [mV] to theta_k in [°]
'''
from numpy import *
from upAndDown import upAndDown
#from Fit import hystFit
# Get data for storing the fit results to speed it up
#data  = genfromtxt('../Daten/hysterese.txt')
#dataUp, dataDo = upAndDown(data)
#fitUp = hystFit(dataUp)
#print fitUp(0) 

def func(x, a, b, c,d,e):     return e*x**4 + d * x**3 + c* x**2 + b*x+ a
def calUpI(xdata): 
    a ,b ,c ,d ,e = 0.352187630864, 25.1127499637, -0.0158345836053, -0.181478576864, 0.000651791965085
    return func(xdata ,a ,b ,c ,d ,e)
def calDoI(xdata): 
    a ,b ,c ,d ,e = 2.52488224945, 25.089094303, -0.0356744534711, -0.181087079036, -0.00137811774661
    return func(xdata ,a ,b ,c ,d ,e)
# TODO make functions for the calibration of V in ° 
# TODO add something for the errors as well 

