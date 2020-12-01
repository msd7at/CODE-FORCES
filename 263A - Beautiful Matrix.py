l=[]
a=0
b=0
for i in range(5):
    x=list(map(int,input().split()))
    if 1 in x:
        a=i
        b=x.index(1)
    l.append(x)
print(abs(2-a) +abs(2-b))
