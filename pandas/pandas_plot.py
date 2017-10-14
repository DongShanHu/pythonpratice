import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

#Series

##data = pd.Series(np.random.randn(1000), index=np.arange(1000))
###randn(1000)數據累加
##data=data.cumsum()


data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )

data=data.cumsum()
#plot 線性圖
#plot method "bar",' hist','box','area',scarrer,hexbin,pie
#data.plot()
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()



##data.plot()
###plt.plot(x=,y=)
##plt.show()
