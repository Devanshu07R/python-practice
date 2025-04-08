import numpy as np

x = np.array([1,2])
print("Integer Datatype:")
print(x.dtype)

x = np.array([1.0,2.0])
print("\nfloat Datatype:")
print(x.dtype)

x = np.array([1,2],dtype = np.int64)
print("\nforcing a datatype:")
print(x.dtype)