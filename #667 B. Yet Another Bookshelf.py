t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    i=0
    while i<n and l[i]==0:
        i+=1
    j=n-1
    while  j>=0 and l[j]==0:
        j-=1
    ct=l.count(1)
    if ct==0:
        print(0)
    else:
        if ct==1:
        
            print(0)
        else:
            c=0
            for k in range(i+1,j):
                if l[k]==0:
                    c+=1
            if c!=0:
                print(c)
            else:
                print(0)
                
                
        
