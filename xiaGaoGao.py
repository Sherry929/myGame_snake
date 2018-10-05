import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Read Yahoo!/ Google finance data
# part 2 question a
da = pd.read_csv('https://www.math.ust.hk/~macwyu/MAFS5110_2018-2019/MAFS5110_2018-2019/Chapter_1/geDJ.txt',sep = "\s+",names = ['date','open','high','low','close','vol'])
log_return = np.diff(np.log(np.array(da["close"])))
#da.index[1:]
da1 = pd.concat([pd.DataFrame(da), pd.DataFrame(log_return)], axis = 1)
da1.columns=['date','open','high','low','close','vol','log_return']
da1.boxplot(column='log_return')

dasp = pd.read_csv('https://www.math.ust.hk/~macwyu/MAFS5110_2018-2019/MAFS5110_2018-2019/Chapter_1/sp500.txt',sep = "\s+")
lgrt_sp = np.diff(np.log(np.array(dasp["close"])))
#da2 =pd.DataFrame(lgrt_sp,index = dasp.index[1:],columns =['log_return'])
da2 = pd.concat([pd.DataFrame(lgrt_sp), pd.DataFrame(log_return)], axis = 1 )
# call concat and pass param axis=1 to concatenate column-wise (axis = 0 is defaulted to concatenate row-wise)
#da2.index =da.index[1:]
da2.columns = ["SP_logreturn","GE_logreturn"]
da2.boxplot(column=['SP_logreturn','GE_logreturn'])
#plt.boxplot(da2, sym = "o")
plt.show()
