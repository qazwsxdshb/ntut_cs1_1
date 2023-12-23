def sol(st,cave,ans=[],path=[],fin=[],dep=0):
    for i in cave:
        if(i[0] not in path and st==i[0]):
            fin.append(sol(i[2],cave,ans+[i[1]],path+[i[0]],fin,dep+1))
            fin.append(sol(i[3],cave,ans+[i[1]],path+[i[0]],fin,dep+1))
    if(dep==0):return fin
    return [sum(ans),path]

start,cave=list(map(int,input().split())),[]
for i in range(start[0]):cave.append(list(map(int,input().split())))
print(max(sol(start[1],cave),key=lambda x:x[0])[0])