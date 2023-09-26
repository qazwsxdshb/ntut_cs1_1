def bowling():
    x,p=[0,0,0,0,0],0
    for _ in range(3):
        x[p]=(int(input()))
        if(p==1 and x[0]<10):
            p+=1
            x[p]=(int(input()))
        p+=1
    if(x[p-1]+x[p-2]>=10 and x[p-1]+x[p-2]<20):
        x[-1]=int(input())
    ans=sum(x)
    tmp,t=0,0
    for i in x:
        if(i==10 and tmp==0):
            ans+=i*2
            tmp=0
            t=0
        elif(i+t==10 and tmp==1):
            ans+=i
            tmp=0
            t=0
        t=i
        tmp+=1
        tmp%=2
    print(ans)

if __name__=='__main__':
    bowling()