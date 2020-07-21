#code
from collections import Counter

def majority(array,n):
    Dictfreq = Counter(array)
    for (element,value) in Dictfreq.items():
         if (value > (n/2)):
            return element
    return -1

if __name__ == "__main__":
    t = int(input())
    arr=[]
    for j in range(0,t):
        n = int(input())
        list1 = list(map(int, input().split()[:n]))
        result = majority(list1,n)
        arr.append(result)

    for i in range(0,t):
        print(arr[i])
