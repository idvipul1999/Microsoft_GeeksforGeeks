def keypair(arr,n,x):
    cnt=0
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==x):
                return(str("Yes"))
            else:
                pass

    return(str("No"))


t =int(input())
for i in range(0,t):
    n,x=map(int,input().split())
    arr=list(map(int, input().split(' ')[:n]))
    result= keypair(arr,n,x)
    print(result)
