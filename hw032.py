def Row(matrix):
    if(1==con(matrix)):
        matrix[matrix.index(0)]=(10-sum(matrix))
    return matrix

def Tr(matrix):
    ans=[]
    for i in range(len(matrix)):
        tmp=[]
        for u in range(len(matrix)):
            tmp.append(matrix[u][i])
        ans.append(tmp)
    return ans

def block(matrix,y,x):
    tmp=matrix[x][y:y+2]+matrix[x+1][y:y+2]
    if(1==con(tmp)):
        try:matrix[x][y+matrix[x][y:y+2].index(0)]=(10-sum(tmp))
        except:None
        try:matrix[x+1][y+matrix[x+1][y:y+2].index(0)]=(10-sum(tmp))
        except:None
    return matrix

def con(matrix,ans=0):
    for i in matrix:
        if(0==i):ans+=1
    return ans

ans,x=[],[]
for i in range(4):
    ans.append(list(map(int,input().split())))

for _ in range(16):
    for i in range(len(ans)):
        ans[i]=Row(ans[i])
    for i in range(2):
        for u in range(2):
            ans=block(ans,i*2,u*0)
    ans=Tr(ans)

for i in ans:
    for u in i:
        print(u,end=" ")
    print()