t=int(input())
for q in range(t):
    n=int(input())
    root=int(n**(0.5))
    if root**2>=n:
        print((2*root)-2)
    elif (root+1)*(root)>=n:
        print((2*root)-2+1)
    else:
        print(2*root)
