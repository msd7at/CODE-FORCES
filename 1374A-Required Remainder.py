t=int(input())
for q in range(t):
    x,y,n=map(int,input().split())
    if (n-(n%x)+y)<=n:
        print(n-(n%x)+y)
    else:
        print(n-(n%x)-(x-y))
