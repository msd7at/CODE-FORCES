t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    kk=1
    c=0
    s=set()
    for i in l:
        if i not in s:
            s.add(i)
            print(i,end=" ")
            c+=1
            if c==n:
                break
    print()
