t=int(input())
for q in range(t):
    a,b=map(int,input().split())
    if 2*a<=b:
        print(a,2*a)
    else:
        print(-1,-1)
