try:
    cla,co=[],0
    for _ in range(3):
        x=[int(input())]
        for i in range(int(input())):
            x.append(int(input()))
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