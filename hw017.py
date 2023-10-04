try:
    cla,co,cl=[],0,["1","2","3","4","5","6","7","8","9","a","b","c"]
    for _ in range(int(input())):
        x=[str(input())]
        for i in range(int(input())):
            c=input()
            if(int(c[0])>=6 or c[1] not in cl):
                a=int("a")
            x.append(c)
        cla.append(x)
    for i in range(len(cla)-1):
        for u in cla[i]:
            for o in range(i+1,len(cla)):
                if(u in cla[o]):
                    co=1
                    print(cla[i][0],",",cla[o][0],",",u,sep="")
    if(co==0):
        print("correct")
except:
    print("-1")