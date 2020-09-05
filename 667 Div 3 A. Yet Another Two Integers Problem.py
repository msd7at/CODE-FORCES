t=int(input())
for q in range(t):
    a,b=map(int,input().split())
    x=abs(a-b)
    d=x%10
    if d==0:
        c=0
    else:
        c=1
    print(int(x/10)+c)
