import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from scipy.optimize import fmin

# Define data path and initialize variables
DATA = './recoilenergydata_EP219.csv'
data = []; num = 0; den = 0.0

def signal(sigma,Er):
	if 5<Er<15:
		return sigma * 20 * (Er - 5)
	elif 15<Er<25:
		return sigma * 20 * (25 - Er)
	return 0

def background(Er):
	return 1000 * math.exp(-Er/10)
@np.vectorize
def logL(sigma):
	val = 0
	for i in range(len(data)):
		val += data[i]*math.log(signal(sigma,i+0.5)+bgEvents[i]) - signal(sigma,i+0.5)
	return val

#load data
for e in file.read(open(DATA)).split('\r\n'):
	d = e.split(",")
	try:
		data.append(float(d[1]))
	except ValueError:
		continue

#plot data histogram
'''
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
dataHist = ax1.bar(range(0,40),data,alpha=0.3)
ax1.set_xlabel(r'$E_R$ (in keV)')
ax1.set_ylabel('Number of events')
ax1.set_title('Experimental Data and Expected Background')
'''
#plot background histogram

bgEvents = []
for e in range(0,40):
	bgEvents.append(background(e+0.5))
#bgHist = ax1.bar(range(0,40),bgEvents,alpha=0.3, color = 'yellow')
#ax1.legend((dataHist[0], bgHist[0]), ('Data', 'Background'))
#plt.show()

#plotting mean signal events

#plot theoretical signal histograms
'''
sigma = [.01,.1,1,10,100]
for s in sigma:
	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)
	meanSigEvents = []
	for e in range(0,40):
		meanSigEvents.append(signal(s,e+0.5))
	meanSigHist = ax2.bar(range(0,40),meanSigEvents,alpha=0.6, color = 'red')
	ax2.set_title(r'Signal Events $\sigma=%5.2ffb$'%(s))
	ax2.set_xlabel(r'$E_R$ (in keV)')
	ax2.set_ylabel('Number of events')
plt.show()
'''
#plot log likelihood
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
sig = np.linspace(0,3,500)
ax3.plot(sig,logL(sig))
ax3.set_title("Log likelihood function")
ax3.set_xlabel(r'$\sigma$')
ax3.set_ylabel(r'$\ln L$')

max_sig = fmin(lambda sig: -logL(sig), 0.1)
plt.figtext(0.7, .82, '$\hat \sigma = %5.4f$' %(max_sig),fontsize = 14)

plt.show()