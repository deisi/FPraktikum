#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
'''
These Functions make up the kalibration for getting from I in [A] to B in [mT] and V [mV] to theta_k in [°]
'''
#from numpy import *
from upAndDown import upAndDown
#data  = genfromtxt('../Daten/Kerr Winkel/Si5mal.txt', delimiter=';')
#dataUp, dataDo = upAndDown(data)
#xDataUp, yDataUp = dataUp.T[0], dataUp.T[1]
#xDataDo, yDataDo = dataDo.T[0], dataDo.T[1]
def func(x, a, b, c,d,e):     return e*x**4 + d * x**3 + c* x**2 + b*x+ a
def calUpI(xdata): 
    a ,b ,c ,d ,e = 0.352187630864, 25.1127499637, -0.0158345836053, -0.181478576864, 0.000651791965085
    return func(xdata ,a ,b ,c ,d ,e)
def calDoI(xdata): 
    a ,b ,c ,d ,e = 2.52488224945, 25.089094303, -0.0356744534711, -0.181087079036, -0.00137811774661
    return func(xdata ,a ,b ,c ,d ,e)
# TODO make functions for the calibration of V in ° 
# TODO add something for the errors as well 
