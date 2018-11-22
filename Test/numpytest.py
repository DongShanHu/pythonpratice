import numpy as np
A=np.arange(12).reshape((3,4))
print(A)

print(np.split(A,3,axis=1))
