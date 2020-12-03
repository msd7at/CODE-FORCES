s=input()
i=0
t=""
while i<len(s):
    if i<len(s)-2:
        if s[i]=="W" and s[i+1]=="U" and s[i+2]=="B":
            if t=="":
                print(t,end="")
            else:
                print(t,end=" ")
            t=""
            i+=3
        else:
            t+=s[i]
            i+=1
 
    else:
        t+=s[i]
        i+=1
if t!="":
    print(t)
