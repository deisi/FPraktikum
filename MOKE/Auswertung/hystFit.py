import numpy as np
import inspect
from upAndDown import upAndDown
import matplotlib.pyplot as plt
from scipy.optimize import minimize, leastsq, curve_fit
from scipy.stats import chi2
from kalibration import calUpI, calDoI
''' Method for Fitting Data with curve_fit from scipy to Data returning the params of the Fit'''

# Get data for testing
#data  = np.genfromtxt('../Daten/hysterese.txt')
#dataUp, dataDo = upAndDown(data)

def hystFitUp(data): # makes the fit with Calibration for up going Current
    xData, yData = calUpI(data.T[0]), data.T[1]
    yerr  = 0.1*yData
    #^print data

    # Minimize with  scipy.optimize.leastsq
    # Model for fitting
    def func(x, a, b, c,d,e):     return e*x**4 + d * x**3 + c* x**2 + b*x+ a 
    def residuals(x,y,a,b,c,d,e): return (y - func(x,a,b,c,d,e))**2
    #def func(x, a, b, c):          a*np.arctan(np.divide(b,c))
    #def residuals(x,y,a,b,c): return (y - func(x,a,b,c))**2

    # Leastsquare Method
    p0             = [1,1,1,1,1] # Starting Values
    plsq, cov      = curve_fit(func, xData, yData, p0, sigma=yerr)
    a, b, c, d, e  = plsq[0], plsq[1], plsq[2], plsq[3], plsq[4]
    np.set_printoptions(precision=2)
    print cov
    yFit = func(xData, a, b, c, d, e)
    def yFitFunc(z): return func(z, a, b, c, d, e) #der Versuch eine Funktion zu returnen
    print "Params for " + "data" +" are:", 'a= ', a,' b= ', b, ' c =', c ,' d= ',d ,' e= ', e

    # Chisquare test
    S              = np.sum(residuals(xData,yData, a, b, c, d, e)/(yerr**2))
    dof            = len(xData)-5 #Put number of Parameters here
    rv             = chi2(dof) 
    chimin, chimax = rv.ppf(0.025), rv.ppf(0.975)
    # two sided pvalue test
    if S >= dof: pvalue = 2*(rv.cdf(S)-1)
    if S <  dof: pvalue = 2*rv.cdf(S)
    #pvalue = rv.cdf(S)
    print 'chimin:' +str('%.2f'%chimin),'chimax:' +str('%.2f'%chimax), 'chisquare:'+ str('%.2f'%S), 'pvalue: '+ str('%.2f'%pvalue)

    # plot Reult
    #plt.figure() 
    #plt.subplot(211) 
    plt.title(r'Kalibration des Magneten')
    plt.errorbar(xData, yData, yerr, fmt='x', label= 'Data', color='g') 
    plt.plot(xData,yFit, label='Fit', color='g')
    plt.xlabel(r'Strom I in $[A]$')
    plt.ylabel(r'Mag. Feld B in $[mT]$') 
    leg = plt.legend(loc='best', fancybox=True)   # Durchsichtige Legend sehr geil 
    leg.get_frame().set_alpha(0.5) 
    #plt.savefig('PrettyPlot.png') 
    #plt.show()
    
    return yFitFunc # returns the fittet function

def hystFitDo(data): # makes the fit with Calibration for down going Current
    xData, yData = calDoI(data.T[0]), data.T[1]
    yerr  = 0.1*yData
    #^print data

    # Minimize with  scipy.optimize.leastsq
    # Model for fitting
    def func(x, a, b, c,d,e):     return e*x**4 + d * x**3 + c* x**2 + b*x+ a 
    def residuals(x,y,a,b,c,d,e): return (y - func(x,a,b,c,d,e))**2
    #def func(x, a, b, c):          a*np.arctan(np.divide(b,c))
    #def residuals(x,y,a,b,c): return (y - func(x,a,b,c))**2

    # Leastsquare Method
    p0             = [1,1,1,1,1] # Starting Values
    plsq, cov      = curve_fit(func, xData, yData, p0, sigma=yerr)
    a, b, c, d, e  = plsq[0], plsq[1], plsq[2], plsq[3], plsq[4]
    np.set_printoptions(precision=2)
    print cov
    yFit = func(xData, a, b, c, d, e)
    def yFitFunc(z): return func(z, a, b, c, d, e) #der Versuch eine Funktion zu returnen
    print "Params for " + "data" +" are:", 'a= ', a,' b= ', b, ' c =', c ,' d= ',d ,' e= ', e

    # Chisquare test
    S              = np.sum(residuals(xData,yData, a, b, c, d, e)/(yerr**2))
    dof            = len(xData)-5 #Put number of Parameters here
    rv             = chi2(dof) 
    chimin, chimax = rv.ppf(0.025), rv.ppf(0.975)
    # two sided pvalue test
    if S >= dof: pvalue = 2*(rv.cdf(S)-1)
    if S <  dof: pvalue = 2*rv.cdf(S)
    #pvalue = rv.cdf(S)
    print 'chimin:' +str('%.2f'%chimin),'chimax:' +str('%.2f'%chimax), 'chisquare:'+ str('%.2f'%S), 'pvalue: '+ str('%.2f'%pvalue)

    # plot Reult
    #plt.figure() 
    #plt.subplot(211) 
    plt.title(r'Kalibration des Magneten')
    plt.errorbar(xData, yData, yerr, fmt='x', label= 'Data', color='g') 
    plt.plot(xData,yFit, label='Fit', color='g')
    plt.xlabel(r'Strom I in $[A]$')
    plt.ylabel(r'Mag. Feld B in $[mT]$') 
    leg = plt.legend(loc='best', fancybox=True)   # Durchsichtige Legend sehr geil 
    leg.get_frame().set_alpha(0.5) 
    #plt.savefig('PrettyPlot.png') 
    #plt.show()
    
    return yFitFunc # returns the fittet function

def hystFit(data): # makes the fit with Calibration from superposition of up and down
    xData, yData = np.divide(np.add(calUpI(data.T[0]), calDoI(data.T[0])),2), data.T[1]
    #xData, yData = data.T[0], data.T[1]
    yerr  = 0.1*yData
    #^print data

    # Minimize with  scipy.optimize.leastsq
    # Model for fitting
    def func(x, a, b, c,d,e):     return e*x**4 + d * x**3 + c* x**2 + b*x+ a 
    def residuals(x,y,a,b,c,d,e): return (y - func(x,a,b,c,d,e))**2
    #def func(x, a, b, c):          a*np.arctan(np.divide(b,c))
    #def residuals(x,y,a,b,c): return (y - func(x,a,b,c))**2

    # Leastsquare Method
    p0             = [1,1,1,1,1] # Starting Values
    plsq, cov      = curve_fit(func, xData, yData, p0, sigma=yerr)
    a, b, c, d, e  = plsq[0], plsq[1], plsq[2], plsq[3], plsq[4]
    np.set_printoptions(precision=2)
    print cov
    yFit = func(xData, a, b, c, d, e)
    def yFitFunc(z): return func(z, a, b, c, d, e) #der Versuch eine Funktion zu returnen
    print "Params for " + "data" +" are:", 'a= ', a,' b= ', b, ' c =', c ,' d= ',d ,' e= ', e

    # Chisquare test
    S              = np.sum(residuals(xData,yData, a, b, c, d, e)/(yerr**2))
    dof            = len(xData)-5 #Put number of Parameters here
    rv             = chi2(dof) 
    chimin, chimax = rv.ppf(0.025), rv.ppf(0.975)
    # two sided pvalue test
    if S >= dof: pvalue = 2*(rv.cdf(S)-1)
    if S <  dof: pvalue = 2*rv.cdf(S)
    #pvalue = rv.cdf(S)
    print 'chimin:' +str('%.2f'%chimin),'chimax:' +str('%.2f'%chimax), 'chisquare:'+ str('%.2f'%S), 'pvalue: '+ str('%.2f'%pvalue)

    # plot Reult
    #plt.figure() 
    #plt.subplot(211) 
    plt.title(r'Kalibration des Magneten')
    plt.errorbar(xData, yData, yerr, fmt='x', label= 'Data', color='g') 
    plt.plot(xData,yFit, label='Fit', color='g')
    plt.xlabel(r'Strom I in $[A]$')
    plt.ylabel(r'Mag. Feld B in $[mT]$') 
    leg = plt.legend(loc='best', fancybox=True)   # Durchsichtige Legend sehr geil 
    leg.get_frame().set_alpha(0.5) 
    #plt.savefig('PrettyPlot.png') 
    #plt.show()
    
    return yFitFunc # returns the fittet function
