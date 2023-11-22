a,b=map(int,input().split())
cave,index=[]," "+str(b)
for i in range(a):
    cave.append(list(map(int,input().split())))
def Solution(cave,index,gold=0):
    ans=""
    x=int(index.split()[-1])
    for i in cave:
        if(i[0]==x):
            x=i
            break
    if(x.count(0)==3 or len(set(index.split()))!=len(index.split())):
        return str(gold)+" "
    ans+=(Solution(cave,index+" "+str(x[2]),gold+x[1]))
    ans+=(Solution(cave,index+" "+str(x[3]),gold+x[1]))
    return ans
print(max(list(map(int,Solution(cave,index).split()))))