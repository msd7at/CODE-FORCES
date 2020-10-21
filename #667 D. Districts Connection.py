t=int(input())
for q in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    # print(a)
    if len(set(a))==1:
        print("NO")
    else:
        print("YES")
        for i in range(1,n):
            if a[i]!= a[0]:
                seco=i
                break
        for i in range(1,n):
            if a[i]!=a[0]:
                print(1,i+1)
            else:
                print(seco+1,i+1)
