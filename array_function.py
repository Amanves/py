from array import *
arr = array("i",[])
n = int(input("Enter the length of an array : "))
for y in range(n):
    x = int(input("Enter the array element : "))
    arr.append(x)
print("array: ",arr)
from numpy import *
print("sin value: ",(sin(arr)))
print("cos value: ",(cos(arr)))
print("tan value: ",(tan(arr)))
print("log value: ",(log(arr)))
print("sqrt value: ",(sqrt(arr)))
print("log value: ",(log(arr)))
print("sum value: ",(sum(arr)))
print("min value: ",(min(arr)))
print("max value: ",(max(arr)))
print("sort value: ",(sort(arr)))
arr2 = array([2,3,6,4])
print("concetanate :",concatenate([arr,arr2]))


