t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=max(l)
    x=l.count(m)
    if x==n:
        print(-1)
    elif x==1:
        print(l.index(m)+1)
    else:
        id=l.index(m)
        if id==0:
            
            i=id
            while i<n and l[i]==m:
                i+=1
            print(i)
        else:
            print(id+1)
        
