def sol(st,ed,tr,tmp=[],path=[],ans=[]):
    if(st==ed):return [tmp]
    for i in tr:
        if((st in i) and (i not in path)):ans+=sol(i[(1+i.index(st))%2],ed,tr,tmp+[i[(1+i.index(st))%2]],path+[i])
    return ans
start,rest,x,fin_fin_ans=list(map(int,input().split())),list(map(int,input().split())),[],[]
for i in (sol(start[1],start[2],[sorted(list(map(int,input().split()))) for _ in range(start[0])])):
    if(i not in x and len(fin_fin_ans)==0 or len(fin_fin_ans)>=len([start[1]]+i)):fin_fin_ans=[start[1]]+i
    x.append(i)
if(len(set(fin_fin_ans) & set(rest))!=0):print(*(set(fin_fin_ans) & set(rest)))
print(*fin_fin_ans if 0!=len(fin_fin_ans) else ["NO"])