t=int(input())
for q in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ma=min(a)
    mb=min(b)
    c=0
    for i in range(n):
        t1=0
        t2=0
        if a[i]>ma:
            t1=a[i]-ma
        if b[i]>mb:
            t2=b[i]-mb
        c+=max(t1,t2)
    print(c)
