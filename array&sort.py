# create an array of 20 numbers and sort the array
# create an array
arr=[20 ,3 ,40,10,54,2,46,76,59,48,78,60,100,56,70,98,65,45,32,1]
temp=0
print(" The Original Array is :",arr)

# sort the array
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print();
# display the elements after sorting
print("elements in after sorting")
for i in range(0,len(arr)):
    print(arr[i],end="  ")
    

import numpy as np

evenOddSumArr = np.array([20, 3, 40, 10, 54, 2, 46, 76, 59, 48, 78, 60, 100, 56, 70, 98, 65, 45, 32, 1])
evenArrSum = 0
oddArrSum = 0

for i in range(len(evenOddSumArr)):
    if (evenOddSumArr[i] % 2 == 0):
        evenArrSum = evenArrSum + evenOddSumArr[i]
    else:
        oddArrSum = oddArrSum + evenOddSumArr[i]

print("The Sum of Even Numbers in evenOddSumArr Array = ", evenArrSum)
print("The Sum of Odd Numbers in evenOddSumArr Array  = ", oddArrSum)