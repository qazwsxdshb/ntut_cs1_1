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
    def sea(ans):
        kk=[u+i for i in "A 2 3 4 5 6 7 8 9 10 J Q K".split() for u in "S H D C".split()]
        if(ans not in kk):int("A")
        return ans
    ans=[]
    a,b,pub=list(map(sea,input().split())),list(map(sea,input().split())),list(map(sea,input().split()))
    c=a+b+pub
    xxx=0
    while c:
        if(c.pop(0) in c):
            xxx=1
            print("Duplicate deal")
    a_ans,b_ans,co=[],[],0
    for u in a:
        tmp=pub.copy()
        tmp.append(u)
        Number,Color=[],[]
        for i in tmp:
            Color.append(i[0])
            if(len(i)==3):Number.append(i[1:])
            else:Number.append(i[-1])
        a_ans.append(Solution(Number,Color))
        for i in range(4):
            tmp=pub.copy()
            tmp.append(u)
            if(co%2==0):
                tmp[i]=a[1]
            else:tmp[i]=a[0]
            Number,Color=[],[]
            for i in tmp:
                Color.append(i[0])
                if(len(i)==3):Number.append(i[1:])
                else:Number.append(i[-1])
            a_ans.append(Solution(Number,Color))
        co+=1
    for u in b:
            tmp=pub.copy()
            tmp.append(u)
            Number,Color=[],[]
            for i in tmp:
                Color.append(i[0])
                if(len(i)==3):Number.append(i[1:])
                else:Number.append(i[-1])
            b_ans.append(Solution(Number,Color))
            for i in range(4):
                tmp=pub.copy()
                tmp.append(u)
                if(co%2==0):
                    tmp[i]=b[1]
                else:tmp[i]=b[0]
                Number,Color=[],[]
                for i in tmp:
                    Color.append(i[0])
                    if(len(i)==3):Number.append(i[1:])
                    else:Number.append(i[-1])
                b_ans.append(Solution(Number,Color))
            co+=1
    if(xxx==0 and max(a_ans)!=max(b_ans)):
        print("A" if max(a_ans)>max(b_ans) else "B",max(a_ans+b_ans))
    elif(max(a_ans)==max(b_ans)):
        print("Tie")
except:print("Error input")