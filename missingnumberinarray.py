import math
import os
import random
import re
import sys

def missing(arr):
    #CODE 1 is here
    prev=arr[0]
    for i in range(1,len(arr)):
        diff = abs(arr[i]-prev)
        if(diff==1):
            prev = arr[i]
        else:
            return(arr[i]-1)

t = int(input())
arr=[]
for j in range(0,t):
    n = int(input())
    list1 = list(map(int, input().split()[:(n-1)]))
    result=missing(list1,n)
    arr.append(result)

for i in range(0,t):
    print(arr[i])
