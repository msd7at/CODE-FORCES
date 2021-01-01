t=int(input())
for q in range(t) :
    n=  int(input())
    s=input()
    az=[]
    ao=[]
    cc=1
    ans=[]
    j=0
    for i in s:
        if i=="0":
            l=len(ao)
            if l==0:
                az.append(cc)
                ans.append(cc)
                cc+=1
            else:
                p=ao.pop()
                az.append(p)
                ans.append(p)

        else:
            l=len(az)
            if l==0:
                ao.append(cc)
                ans.append(cc)
                cc+=1
            else:
                p=az.pop()
                ao.append(p)
                ans.append(p)
        
    print(cc-1)
    print(*ans,end=" ")
    print()
