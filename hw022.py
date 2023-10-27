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
    ans,kk=[],[i+u for i in "A 2 3 4 5 6 7 8 9 10 J Q K".split() for u in "S H D C".split()]
    co,name,tmp,tmp2=0,[],[],[]
    for _ in range(int(input())):
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
        for z in x:
            if(z not in kk):int("a")
        if(co==0):ans.append([Solution(Number,Color),ii])
    if(co==0):
        while ans:
            tmp,addr=0,0
            for i in range(len(ans)):
                if(tmp<ans[i][0]):
                    tmp=ans[i][0]
                    addr=i
            x=ans.pop(addr)
            print(x[1],x[0])
    else:print("Duplicate deal")
except:print("Error input")