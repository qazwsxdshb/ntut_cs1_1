cla=[]
for _ in range(3):
    x=[int(input())]
    for i in range(int(input())):
        x.append(int(input()))
    cla.append(x)

for i in range(2):
    for u in cla[i]:
        for o in range(i+1,3):
            if(u in cla[o]):
                print(cla[i][0],",",cla[o][0],",",u,sep="")
