t=int(input())
for q in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    for i in range(n-2,-1,-1):
        if k:
            l[n-1]+=l[i]
            k-=1
            l[i]=0
        else:
            break
    l.sort()
    print(l[n-1]-l[0])
