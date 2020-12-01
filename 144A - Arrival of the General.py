n=int(input())
l=list(map(int,input().split()))
ma=max(l)
mxid=l.index(ma)
mi=min(l)
for i in range(n-1,-1,-1):
    if l[i]==mi:
        mnid=i
        break
if mnid < mxid:
    c1=mxid
    c2=n-1-(mnid+1)
    print(c1+c2)
else:
    c1=mxid
    c2=n-mnid-1
    print(c1+c2)
