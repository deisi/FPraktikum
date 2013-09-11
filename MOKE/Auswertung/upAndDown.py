#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#  0. You just DO WHAT THE FUCK YOU WANT TO.
'''
This function makes two sets of data out of given data for hysterese plots
'''
from numpy import *
#data  = genfromtxt('../Daten/Kerr Winkel/Si5mal.txt', delimiter=';')

def upAndDown(data):
    ''' makes two sets of data out of the given Hysterese data sets. One will be for the upgoing and one for the down going '''
    # TODO enter example here
    
    tData  = data.T
    xData  = tData[0]
    yData  = tData[1]
    maxInd = argmax(xData)
    dataUp = transpose([xData[:maxInd+1],yData[:maxInd+1]])
    dataDo = transpose([xData[maxInd+1:],yData[maxInd+1:]])
    return dataUp, dataDo
