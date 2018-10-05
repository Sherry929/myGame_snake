# 导入需要用到的库
from statsmodels import regression
import statsmodels.api as sm
import scipy.stats as stats
import scipy.spatial.distance as distance
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import h5py
import jqdatasdk
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

h5data=h5py.File("C:/Users/anivia/Desktop/5140/data/data_format2_201801.h5",mode='r')
print(list(h5data.keys())[:10])
# 取得股票的价格
start = '2018-01-01 00:00:00'
end = '2018-01-01 00:09:00'
asset = avg('600196.XSHG', fields='price', start_date=start, end_date=end)
dates = asset.index

# 画出价格随时间变化的图像
_, ax = plt.subplots()
ax.plot(asset)
ticks = ax.get_xticks()
ax.set_xticklabels([dates[i].date() for i in ticks[:-1]]) # Label x-axis with dates

# 拟合
X = np.arange(len(asset))
x = sm.add_constant(X)
model = regression.linear_model.OLS(asset, x).fit()
a = model.params[0]
b = model.params[1]
Y_hat = X * b + a
plt.plot(X, Y_hat, 'r', alpha=0.9);
plt.ylabel('Price')
plt.legend(['600196.XSHG', 'Trendline']);

#加载pandas包和os包
#import pandas as pd
#import os
#获取工作目录
#os.getcwd()
#把数据放入工作目录当中，并读取
#stock_data = pd.read_csv(r'000300.csv', parse_dates=[1],encoding='gb2312')
h5data.head()
#把数据从远到近排列
h5data.sort('time', inplace=True)
h5data.head()
#计算5日，20日和60日移动平均线
ma=20
h5data['ma_'+str(ma)]=pd.rolling_mean(h5data['close'],ma)
#h5data.to_csv('000300_ma.csv',index=False)

#30天的股票收盘价
sp=np.array([333.53,334.3,340.98,343.55,338.55,343.51,347.64,352.15,354.87,348,353.54,356.71,357.55,360.5,356.52,349.52,337.72,338.61,338.37,344.8,351.12,347.68,348.4,355.92,357.75,351.31,352.25,350.6,344.9])
N=5
n=np.ones(N)
weights=n/N
print(weights)
sma=np.convolve(weights,sp)[N-1:-N+1]
t=np.arange(N-1,len(sp))
plot(t,sp[N-1:],lw=1)
plot(t,sma,lw=2)
show()
