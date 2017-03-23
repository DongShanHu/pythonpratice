import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan

##處理丟失數據
print(df.dropna(axis=0,how='any'))# how={'any'all}

#將丟失數據填入 數值
#print(df.fillna(value=0))

#看是否有缺失
#print(df.fillna(value=0))

print(np.any(df.isnull())==True)

