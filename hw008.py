try:
    cla,co,cl=[],0,["1","2","3","4","5","6","7","8","9","a","b","c"]
    for _ in range(3):
        x=[str(input())]
        for i in range(int(input())):
            c=input()
            if(int(c[0])>=6 or c[1] not in cl):
                a=int("a")
            x.append(c)
        cla.append(x)

    for i in range(2):
        for u in cla[i]:
            for o in range(i+1,3):
                if(u in cla[o]):
                    co=1
                    print(cla[i][0],",",cla[o][0],",",u,sep="")
    if(co==0):
        print("correct")
except:
    print("-1")