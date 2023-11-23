def Solution(tmp,index=0):
    if(tmp==0 or tmp==1):
        return index
    if(tmp%2==0):
        return Solution(tmp//2,index+1)
    else:
        return Solution((tmp+1)//2,index+1)
ans=[]
while 1:
    ans.append(bin(Solution(int(input(),2)))[2:])
    if "-1"==input():break
for i in ans:
    print("0"*(4-len(i))+i)