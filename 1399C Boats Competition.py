def ppr(l,n):
    m=0
    for k in range(1,101):
        lo=0
        h=n-1
        c=0
        while lo<h:
            s=l[lo]+l[h]
            if s==k:
                c+=1
                m=max(m,c)
                lo+=1
                h-=1
            elif s<k:
                lo+=1
            else:
                h-=1
    print(m)
if __name__=='__main__':
    t=int(input())
    for q in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        l.sort()
        ppr(l,n)
