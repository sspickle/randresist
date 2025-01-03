
import numpy as np
import random

rvals = np.array([float(x) for x in "1.0 1.1 1.2 1.3 1.5 1.6 1.8 2.0 2.2 2.4 2.7 3.0 3.3 3.6 3.9 4.3 4.7 5.1 5.6 6.2 6.8 7.5 8.2 9.1".split()])

def getRList(low, high):
    vals = np.empty(0,float)

    l10 = np.log(10)
    logLow = int(np.floor(np.log(low)/l10 + 0.0001))
    logHigh = int(np.floor(np.log(high)/l10 + 0.001))
    for p in range(logLow, logHigh+1):
        vals = np.append(vals,rvals*10**p)

    vals = vals[np.where((vals <= high) & (vals >= low))]
    vals = np.unique(vals)
    vals = sorted(vals)
    return vals

def getRandomResistor(low, high, N=1):
    """
    Return a realistic random resistor in this range
    """
    vals = getRList(low, high)
    if N == 1:
        result = random.choice(np.unique(vals))
    else:
        result = random.choice(np.unique(vals),size=N)

    return result

if __name__=='__main__':
    print(getRList(12,29))
    
