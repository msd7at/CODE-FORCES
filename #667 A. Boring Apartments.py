import math
t=int(input())
for q in range(t):
    n=int(input())
    a=[1,2,3,4]
    l=[1,2,3,4,5,6,7,8,9]
    f=n%10
    le=int(math.log(n,10))+1
    ans=0
    c=0
    ans=10*(f-1)
    for i in range(le):
        ans=ans+a[c]
        c=(c+1)%4
    print(ans)
        
