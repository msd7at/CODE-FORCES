s=input()
l=0
m=0
r=len(s)-1
s=list(s)
while m<=r:
    if s[m]=="1":
        s[m],s[l]=s[l],s[m]
        m+=2
        l+=2
    elif s[m]=="3":
        s[m],s[r]=s[r],s[m]
        r-=2
    else:
        m+=2
print("".join(s))
