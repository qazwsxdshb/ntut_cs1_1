class_name,cla=[],[]
for _ in range(int(input())):
    class_name.append(input())
    tmp=[]
    for i in range(int(input())):
        tmp.append(int(input()))
    cla.append(tmp)
for i in range(len(cla)):
    for u in range(i+1,len(cla)):
        for t in cla[u]:
            if(t in cla[i]):
                print(class_name[i],"and",class_name[u],"conflict on",t)