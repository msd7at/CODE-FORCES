t=int(input())
for q in range(t):
    x,y,k=map(int,input().split())
    a=int((k)+(k*y)-1)
    ans=a//(x-1)
    if ans*(x-1) !=a:
        ans+=1
    ans+=k
    print(ans)
