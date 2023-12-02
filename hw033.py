def cal(a,b,x=0,y=0,z=0):
    if(min(a[1],b[1])<0):x=abs(min(a[1],b[1]))
    if(min(a[2],b[2])<0):y=abs(min(a[2],b[2]))
    if(min(a[3],b[3])<0):z=abs(min(a[3],b[3]))
    return [a[0],b[0],(((a[1]+x)-(b[1]+x))**2+((a[2]+y)-(b[2]+y))**2+((a[3]+z)-(b[3]+z))**2)**0.5]

tmp,ans=[],[]
for i in range(int(input())):
    tmp.append(list(map(int,input().split())))

for i in range(len(tmp)):
    for u in range(i+1,len(tmp)):
        ans.append(cal(tmp[i],tmp[u]))
ans=sorted(ans,key=lambda x:x[2])
for i in range(3):
    x=ans[i]
    print(x[0],x[1]," ".join([str(i) for i in tmp[x[0]-1][1:]])," ".join([str(i) for i in tmp[x[1]-1][1:]]))