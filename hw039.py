def matrix(arr,size,sel):
    ans=[]
    for _ in range(size):
        tmp=[]
        for _ in range(size):
            x=arr.pop(0)
            if(x in sel):tmp.append("A")
            else:tmp.append(x)
        ans.append(tmp)
    return ans


size,sel=int(input()),int(input())
A=input().split()
B=input().split()

sel=input().split()
A=matrix(A,size,sel)
B=matrix(B,size,sel)
def Sol(matrix,ans=0):
    for i in matrix:
        if(len(set(i))==1):ans+=1
    for i in range(len(matrix)):
        a=set()
        for u in range(len(matrix)):
            a.add(matrix[u][i])
        if(len(a)==1):ans+=1
    a=set()
    for i in range(len(matrix)):
        a.add(matrix[i][i])
    if(len(a)==1):ans+=1
    a=set()
    for i in range(len(matrix)):
        a.add(matrix[i][len(matrix)-1-i])
    if(len(a)==1):ans+=1
    return ans

if Sol(A)>Sol(B):print("A Win")
elif Sol(A)<Sol(B):print("B Win")
else:print("Tie")
