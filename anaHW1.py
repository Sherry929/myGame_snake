# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:35:09 2018

@author: anivia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import ttest_ind
import statsmodels.stats.api as sms
GE=pd.read_csv('C:/Users/anivia/Desktop/geDJ.txt',sep="\s+",header=None,names=['date','open','high','low','close','vol'])
SP=pd.read_csv('https://www.math.ust.hk/~macwyu/MAFS5110_2018-2019/MAFS5110_2018-2019/Chapter_1/sp500.txt',sep = "\s+")
logreturn_GE=np.diff(np.log(np.array(GE["close"])))
logreturn_sp500 = np.diff(np.log(np.array(SP["close"])))
da2 = pd.concat([pd.DataFrame(logreturn_GE), pd.DataFrame(logreturn_sp500)], axis = 1)
#da2.columns=['date','open','high','low','close','vol','logreturn_sp500']
#da2.index=da.index[1:]
da2.columns = ["logreturn_GE","logreturn_sp500"]
da2.boxplot(column=['logreturn_GE','logreturn_sp500'])
plt.show()
print(stats.mood(logreturn_sp500,logreturn_GE))
print('H0 can be rejected, the variances are significantly different')
print(ttest_ind(logreturn_sp500,logreturn_GE,equal_var=True))
print('')
cm=sms.CompareMeans(sms.DescrStatsW(logreturn_sp500),sms.DescrStatsW(logreturn_GE))
print(cm.tconfint_diff())
