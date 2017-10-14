#pandas merge

import pandas as pd

#merging two df by keys (may be used in database)

'''
#定義資料
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
#    A   B key
# 0  A0  B0  K0
# 1  A1  B1  K1
# 2  A2  B2  K2
# 3  A3  B3  K3

print(right)
#    C   D key
# 0  C0  D0  K0
# 1  C1  D1  K1
# 2  C2  D2  K2
# 3  C3  D3  K3

####依据key column合并，并打印出
res = pd.merge(left, right, on='key')

print(res)


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})


'''

'''
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print(left)
print(right)
'''



#依据key1和key2 columns进行合并，并打印出四种结果['left', 'right', 'outer', 'inner']
#default 的合併是inner
#res = pd.merge(left, right, on=['key1', 'key2'],how='inner')

#res = pd.merge(left, right, on=['key1', 'key2'],how='right')
#res = pd.merge(left, right, on=['key1', 'key2'],how='left')

#give a indicator to custome 預設欄位是merge
#res = pd.merge(left, right, on=['key1', 'key2'],how='outer',indicator=True)
#print(res)

#   col1 col_left  col_right      _merge
# 0   0.0        a        NaN   left_only
# 1   1.0        b        2.0        both
# 2   2.0      NaN        2.0  right_only
# 3   2.0      NaN        2.0  right_only

#res = pd.merge(left, right, on=['key1', 'key2'],how='outer',indicator='indicator_column')


#print(res)
#依据左右资料集的index进行合并，how='outer',并打印出
#left_index ,right_index
#res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
#res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
#print(res)
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
#使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'])
print(res)




