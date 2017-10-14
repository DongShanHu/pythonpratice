import pandas as pd
import numpy as np
'''
#concatenating
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['A', 'B', 'C', 'D'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['A', 'B', 'C', 'D'])
print(df1)
print(df2)
print(df3)


##axis=0直向合併 axis=1橫向合併 ignore_index=True 將數字轉為連續012->12345678
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)
'''

'''
#join,['inner','outer'],預設的是outer 
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['B', 'C', 'D', 'E'])
res=pd.concat([df1,df2],join='inner',ignore_index=True)
print(res)
'''

'''
#join_axes
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['A', 'B', 'C', 'D'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['B', 'C', 'D', 'E'], index=[2,3,4])
res=pd.concat([df1,df2],axis=1,join_axes=[df1.index])
print(res)
'''


#append 往下面加一個數據 但append沒有橫向數據，因為append 沒有axis參數
'''
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['A', 'B', 'C', 'D'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['A', 'B', 'C', 'D'])
res=df1.append([df2,df3],ignore_index=True)
print(res)

'''

'''
#append insert 一行數據
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['A', 'B', 'C', 'D'])
df4=pd.Series([1,2,3,4],index=['A', 'B', 'C', 'D'])
res=df1.append(df4,ignore_index=True)
print(res)
'''
