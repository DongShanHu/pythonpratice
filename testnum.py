
##NUMPY 的屬性
##import numpy as np
##array=np.array([[1,2,3],[2,3,4]])
##print(array)
##print('number of dim',array.ndim)
##print('shape:',array.shape)
##print('shape:',array.size)


##array 的建立-numpy
##import numpy as np
##a=np.array([[2,23,4],
##            [2,3,4]])

##a=np.ones((3,4))

##a=np.arange(12).reshape((3,4))
##a=np.linspace(1,10,5)
##print(a)

import numpy as np
##a=np.array([[1,1],
##            [0,1]])
##b=np.arange(4).reshape((2,2))
##cdot=np.dot(a,b)
##cdot2=a.dot(b)
##print(cdot2)
##print(cdot)

##c=10*np.sin(a)

##print(c)

##print(b)
##print(b<3)

a=np.random.random((2,4))

print(a)
print(np.sum(a,axis=1))
print(np.min(a,axis=0))
