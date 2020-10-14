t=int(input())
for q in range(t):
    n,m=map(int,input().split())
    flag=0
    for i in range(n):
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if b==c:
            flag=1
    if m%2==1:
        print("NO")
    else:
        if not flag:
            print("NO")
        else:
            print("YES")
