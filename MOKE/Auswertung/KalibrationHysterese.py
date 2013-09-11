import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, leastsq, curve_fit
from scipy.stats import chi2
''' Method for Fitting Data with curve_fit from scipy '''

# Get data Up
data  = np.genfromtxt('../Daten/hystereseUp.txt')
xData = data.T[0]
yData = data.T[1]
yerr  = 5*np.ones(len(xData))
#^print data

# Minimize with  scipy.optimize.leastsq
# Model for fitting
def func(x, a, b, c,d,e):     return e*x**4 + d * x**3 + c* x**2 + b*x+ a 
def residuals(x,y,a,b,c,d,e): return (y - func(x,a,b,c,d,e))**2

# Leastsquare Method
p0             = [1,1,1,1,1] # Starting Values
plsq, cov      = curve_fit(func, xData, yData, p0, sigma=yerr)
a, b, c, d, e  = plsq[0], plsq[1], plsq[2], plsq[3], plsq[4]
np.set_printoptions(precision=2)
print cov
yFit = func(xData, a, b, c, d, e)
print "Param for UpFit ist:", 'a= ', a,' b= ', b, ' c =', c,' d= ', d,' e= ', e

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
#plt.title(r'Ein vielsagender Titel')
plt.errorbar(xData, yData, yerr, fmt='o', label= r'Up', color='r') 
plt.plot(xData,yFit, label='Up Fit', color='r')
#plt.xlabel(r'x-achse $[m]$')
#plt.ylabel(r'y-achse $[s]$') 
#leg = plt.legend(loc='best', fancybox=True)   # Durchsichtige Legend sehr geil 
#leg.get_frame().set_alpha(0.5) 
#plt.savefig('PrettyPlot.png') 

# Get data Down
data  = np.genfromtxt('../Daten/hystereseDown.txt')
xData = data.T[0]
yData = data.T[1]
yerr  = 5*np.ones(len(xData))
#print data

# Minimize with  scipy.optimize.leastsq
# Model for fitting
def func(x, a, b, c,d,e):     return e*x**4 + d * x**3 + c* x**2 + b*x+ a 
def residuals(x,y,a,b,c,d,e): return (y - func(x,a,b,c,d,e))**2

# Leastsquare Method
p0             = [1,1,1,1,1] # Starting Values
plsq, cov      = curve_fit(func, xData, yData, p0, sigma=yerr)
a, b, c, d, e  = plsq[0], plsq[1], plsq[2], plsq[3], plsq[4]
np.set_printoptions(precision=2)
print cov
yFit = func(xData, a, b, c, d, e)
print "Param for DoFit ist:", 'a= ', a,' b= ', b, ' c =', c,' d= ', d,' e= ', e


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
plt.title(r'Hysterese des Magneten')
plt.errorbar(xData, yData, yerr, fmt='x', label= r'Down', color='g') 
plt.plot(xData,yFit, label='Down Fit', color='g')
plt.xlabel(r'Strom I in $[A]$')
plt.ylabel(r'Mag. Feld B in $[mT]$') 
leg = plt.legend(loc='best', fancybox=True)   # Durchsichtige Legend sehr geil 
leg.get_frame().set_alpha(0.5) 
#plt.savefig('PrettyPlot.png') 
plt.show()


