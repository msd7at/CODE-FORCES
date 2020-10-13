t=int(input())
for q in range(t):
    n,x=map(int,input().split())
    if n==1 or n==2:
        print(1)
    else:
        i=1
        l=3
        while True:
            i+=1
            if l<=n <=(x*(i-1)+2):
                print(i)
                break
            l=1+(x*(i-1)+2)
