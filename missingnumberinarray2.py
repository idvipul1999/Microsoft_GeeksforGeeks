import math
import os
import random
import re
import sys

def missing(array,n):
    res=[]
    addition = sum(range(1,n+1))
    for i in range(0,len(array)):
        addition = addition - array[i]
    return addition

t = int(input())

arr=[]
for j in range(0,t):
    n = int(input())
    list1 = list(map(int, input().split()[:(n-1)]))
    result=missing(list1,n)
    arr.append(result)

for i in range(0,t):
  print(arr[i])
