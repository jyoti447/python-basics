import numpy as np
arr1= np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
a= arr1.reshape(2,2)
b= arr2.reshape(2,2)
print("array 1 =",a)
print("array 2 = ",b)

c =np.dot(a,b)
print("final array is =",c)