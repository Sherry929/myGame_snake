import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.stats.api as sms
import scipy.stats as stats
from scipy.stats import ttest_1samp,shapiro,kstest,anderson,wilcoxon
from scipy.stats import ttest_ind
da=pd.read_csv('C:/Users/anivia/Desktop/geDJ.txt',sep="\s+",header=None,names=['date','open','high','low','close','vol'])
rt = np.diff(np.log(np.array(da["close"])))
da1 = pd.concat([pd.DataFrame(da), pd.DataFrame(rt)], axis = 1)
da1.columns=['date','open','high','low','close','vol','return_GE']
da1.boxplot(column='return_GE')
plt.show()

a=da1['return_GE'].mean()
b=da1['return_GE'].var()
c=da1['return_GE'].skew()		# adjusted (or unbiased) skewness
d=da1['return_GE'].kurtosis()	# adjusted (or unbiased) excess kurtosis
print('***a***')
print('Sample mean={}'.format(a))
print('sample variance={}'.format(b))
print('sample akewness={}'.format(c))
print('sample excess kurtosis={}'.format(d))
#print(da1)

z=(rt-rt.mean())/rt.std()
sm.qqplot(z,line='45')
#plt.show()
#H0：the population mean of the log return is equal to 0
#H1: the population mean of the log return is not equal to 0

e=ttest_1samp(rt,0)
print(e)
CI=sms.DescrStatsW(rt).tconfint_mean(alpha=0.05,alternative='two-sided')
print('95% C.I.is ',CI)
print('Mu=0 is inside this C.I. and pvalue>0.05, do not reject H0, hence Mu_ge is equal to 0')
print('***e***')
f=shapiro(rt)
print('Shapiro-Wilk:',f)
z1=(rt-np.mean(rt))/np.std(rt)
g=kstest(z1,cdf='norm')
print('Kolmogorov-Smirnov:',g)
h=anderson(rt,dist='norm')
print('Anderson-Darling:',h)
print('the conclusion is: the Statistic > critical_values,hence p-value<0.01, H0 can be rejected.')

print('***f***')
print(wilcoxon(rt-0, correction = False))
#print(np.mean(rt))
#print(wilcoxon(rt-0.1, correction = True))
#print(wilcoxon(rt-np.mean(rt), correction = True))
print('Mu_ge equal 0')

print('***')
GE=pd.read_csv('C:/Users/anivia/Desktop/geDJ.txt',sep="\s+",header=None,names=['date','open','high','low','close','vol'])
SP=pd.read_csv('https://www.math.ust.hk/~macwyu/MAFS5110_2018-2019/MAFS5110_2018-2019/Chapter_1/sp500.txt',sep = "\s+")
logreturn_GE=np.diff(np.log(np.array(GE["close"])))
logreturn_sp500 = np.diff(np.log(np.array(SP["close"])))
da2 = pd.concat([pd.DataFrame(logreturn_GE), pd.DataFrame(logreturn_sp500)], axis = 1)
da2.columns = ["logreturn_GE","logreturn_sp500"]
da2.boxplot(column=['logreturn_GE','logreturn_sp500'])
#plt.show()

print('***')
print(stats.mood(logreturn_sp500,logreturn_GE))
print('H0 can be rejected, the variances are significantly different')
print(ttest_ind(logreturn_sp500,logreturn_GE,equal_var=True))
print('Means are insignificantly different')
#cm=sms.CompareMeans(sms.DescrStatsW(logreturn_sp500),sms.DescrStatsW(logreturn_GE))
#print('C.I. is ',cm.tconfint_diff())
print('so they are not equal.')
from scipy.stats import ranksums
print(ranksums(logreturn_sp500, logreturn_GE))
print('two groups do not have equal meDIans')