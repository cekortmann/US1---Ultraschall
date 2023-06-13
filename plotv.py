import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  

n,t= np.genfromtxt('geschw.txt', unpack= True, skip_header=1)
n, aun, aob, d = np.genfromtxt('block.txt', unpack= True, skip_header=3, skip_footer=2)

def g(x,a,b):
    return a*x+b

para,pcov =curve_fit(g,t,aob)#,p0=[1,mean,sigma])
a,b = para
pcov = np.sqrt(np.diag(pcov))
fa, fb = pcov
ua = ufloat(a, fa) 
ub = ufloat(b, fb)

xx= np.linspace(0,9,100)


print('ua',ua)
print('ub',ub)
plt.plot(xx, g(xx, *para), 'orange', linewidth = 1, label = 'Ausgleichsfunktion', alpha=0.5)
plt.plot(t, aob, 'xb', markersize=6 , label = 'Beschleunigung (V>0)', alpha=0.5)
plt.xlabel(r'$t \, / \, \mathrm{\mu s}$')
plt.ylabel(r'Abstand von oben$\mathrm{/} \mathrm{mm}$')
plt.legend(loc="best")                  # legend position
plt.grid(True)                          # grid style
plt.savefig('build/plotv.pdf', bbox_inches = "tight")
plt.clf() 