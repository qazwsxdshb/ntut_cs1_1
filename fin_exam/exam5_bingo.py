size=int(input().split()[0])
def inarray(size):
    tmp=list(map(int,input().split()))
    return tmp
def inbingo(size,tmp):
    ans=[]
    for i in range(0,len(tmp),size):
        ans.append(tmp[i:i+size])
    return ans
a,b=inarray(size),inarray(size)
add=inbingo(size,a)
bdd=inbingo(size,b)

for i in list(map(int,input().split())):
    a[a.index(i)]=0
    b[b.index(i)]=0

def cal(size,tmp,dd):
    ans,ans2=0,0
    # row
    for i in range(size):
        co=tmp[i].count(0)
        if(co==size):
            ans+=1
            ans2+=sum(dd[i])
    # col
    for u in range(size):
        co,v=0,0
        for i in range(size):
            if(0==tmp[i][u]):
                co+=1
                v+=dd[i][u]
        if(co==size):
            ans+=1
            ans2+=v
    co,v=0,0
    # left up to right down 
    for i in range(size):
        if(0==tmp[i][i]):
            co+=1
            v+=dd[i][i]
    if(co==size):
        ans+=1
        ans2+=v
    co,v=0,0
    # right up to left down 
    for i in range(size):
        if(0==tmp[i][size-1-i]):
            co+=1
            v+=dd[i][size-1-i]
    if(co==size):
        ans+=1
        ans2+=v
    return ans,ans2
a,a1=cal(size,inbingo(size,a),add)
b,b1=cal(size,inbingo(size,b),bdd)
if(a>b):print("A Win")
elif(a<b):print("B Win")
else:
    if(a1>b1):print("A Win")
    elif(a1<b1):print("B Win")
    else:print("Tie")