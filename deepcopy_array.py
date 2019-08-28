from numpy import *
arr1 = array([2,3,4,5])
arr2 = arr1.copy()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
arr1[2] = 8
print(arr1)
print(arr2)