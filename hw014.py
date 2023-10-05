x,p=[0]*20,0
for _ in range(10):
    x[p]=(int(input()))
    p+=1
    if(p%2==1 and x[p-1]==10):pass
    elif(p%2==1):
        x[p]=(int(input()))
    p+=1

if(x[-2]==10):
    x.append(int(input()))
    x.append(int(input()))
elif(x[-1]+x[-2]==10):
    x.append(int(input()))

ans=sum(x)

for i in range(0,9):
    if(x[i*2]==10):
        l=0
        for o in range(i*2+2,len(x)):
            if(x[o]!=0):
                l+=1
                ans+=x[o]
            if(l==2):
                break
    elif(x[i*2]+x[i*2+1]==10):
        for o in range(i*2+2,len(x)):
            if(x[o]!=0):
                ans+=x[o]
                break
print(ans)