pri=[[380],[1200],[180]]
co=0
cl=["A","B","C"]
x,tmp=[],[]
for i in range(3):
    p=0
    for u in input().split(","):
        p+=1
        if(p==1):
            x.append(int(u))
        else:
            pri[i].append(int(u))
for i in x:
    ans=0
    i=int(i)
    if(11<=i and i<=20):
        ans+=i*pri[co][1]*pri[co][0]*0.01
    elif(21<=i and i<=30):
        ans+=i*pri[co][2]*pri[co][0]*0.01
    elif(i>=31):
        ans+=i*pri[co][3]*pri[co][0]*0.01
    else:
        ans+=i*pri[co][0]
    co+=1
    tmp.append(int(ans+1) if ans>int(ans) else int(ans))
print(cl[tmp.index(int(max(tmp)))],",",int(max(tmp)),sep="")
print(cl[tmp.index(int(sum(tmp)-max(tmp)-min(tmp)))],",",int(sum(tmp)-max(tmp)-min(tmp)),sep="")
print(cl[tmp.index(int(min(tmp)))],",",int(min(tmp)),sep="")
print(int(sum(tmp)))