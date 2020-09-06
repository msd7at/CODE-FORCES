t=int(input())
def pro(a,b,x,y,n):
    d1=a-x
    d2=b-y
    c1=min(n,d1)
    a=a-c1
    n=n-c1
    c2=min(n,d2)
    b=b-c2
    n=n-c2
    return (a*b)
        
for q in range(t):
    a,b,x,y,n=map(int,input().split())
    print(min(pro(a,b,x,y,n),pro(b,a,y,x,n)))
