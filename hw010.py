def bowling():
    x,p=[0,0,0,0,0],0
    for _ in range(3):
        x[p]=(int(input()))
        if(p==1 and x[0]<10):
            p+=1
            x[p]=(int(input()))
        elif(p==0 and x[0]==10):
            p+=1
        p+=1
    if(x[3]+x[2]>=10):
        x[-1]=int(input())
    ans=sum(x)
    if(x[0]==10):
        ans+=x[2]+x[3]
    elif(x[0]+x[1]==10):
        ans+=x[2]
    print(ans)

if __name__=='__main__':
    bowling()