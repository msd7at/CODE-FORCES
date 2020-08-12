t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    k=1
    
    for i in range(1,n):
        if abs(l[i]-l[i-1])>1:
            
            print("NO")
            k=0
            break
    if k==1:
        print("YES")
