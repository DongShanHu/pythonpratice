from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'])

df['F']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
print(df)
'''
print(df['A'], df.A)
print(df[0:3], df['20130102':'20130104'])

# select by label: loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df.loc['20130102', ['A','B']])

# select by position: iloc
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])

#增加空行
#df['F']=np.nan
#增加一列 pd.Series
#df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6)


# mixed selection: ix
print(df.ix[:3, ['A', 'C']])
# Boolean indexing
print(df[df.A > 0])
'''

