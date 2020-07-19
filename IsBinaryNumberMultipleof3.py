def binary(bn):
    i=0
    sum=0
    while(bn!=0):
        ld = bn%10
        bn = bn//10
        sum=ld*pow(2,i)+sum
        i+=1
    if(sum%3==0):
        return(1)
    else:
        return(0)



n = int(input())
for i in range(n):
    bn= int(input())
    result = binary(bn)
    print(result)
