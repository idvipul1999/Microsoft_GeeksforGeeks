#code
def rotatedindex(array, x):

  for i in range(0,n):
      if(x==array[i]):
          return i
  return -1

if __name__ == "__main__":
    t = int(input())
    arr=[]
    for j in range(0,t):
        n = int(input())
        list1 = list(map(int, input().split()[:n]))
        x = int(input())
        result = rotatedindex(list1, x)
        arr.append(result)

    for i in range(0,t):
        print(arr[i])
