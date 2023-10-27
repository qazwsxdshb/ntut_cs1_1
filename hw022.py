def Solution(Number,Color,tmp=0) -> int:
    ans=[]
    for i in range(13):
        Nu=[]
        for u in range(1,6):
            x=(i+u)%14+(i+u)//14
            if(x==13):Nu.append("K")
            elif(x==12):Nu.append("Q")
            elif(x==11):Nu.append("J")
            elif(x==1):Nu.append("A")
            else:Nu.append(str(x))
        ans.append(sorted(Nu))
    for i in ans:
        if (all(sorted(Number)[u]==i[u] for u in range(len(Number))) and len(set(Color))==1):return 9
    for i in set(Number):
        if Number.count(i)==4:return 8
    if(len(set(Number))==2):return 7
    if(len(set(Color))==1):return 6
    for i in ans:
        if all(sorted(Number)[u]==i[u] for u in range(len(Number))):return 5
    for i in set(Number):
        if Number.count(i)==3:return 4
    for i in set(Number):
        if Number.count(i)==2:tmp+=1
    if(tmp==2):return 3
    if(tmp==1):return 2
    return 1

try:
    ans={}
    co,name,tmp,tmp2=0,[],[],[]
    xx=int(input())
    if(1>=xx or xx>=6):int("A")
    for _ in range(xx):
        x=(input().split())
        if(len(x)!=6):int("a")
        name.append(x.pop(0))
        tmp.append(x)
        tmp2=tmp2+x
    while tmp2:
        if(tmp2.pop(0) in tmp2):co=1
    for x,ii in zip(tmp,name):
        Color=(lambda x:[i[-1] for i in x])(x)
        Number=[]
        for i in x:
            if i[:2]=="10":Number.append("10")
            else:Number.append(i[0])
        for i,u,z in zip(Color,x,Number):
            if(z not in "A12345678910JQK" or i not in "SHDC"):int("a")
            elif(len(u)!=2 and z!="10"):int("a")
        if(co==0):ans.update({ii:Solution(Number,Color)})
    if(co==0):
        for i in dict(sorted(ans.items(), key=lambda x:x[1],reverse=True)):
            print(i,ans[i])
    else:print("Duplicate deal")
except:print("Error input")