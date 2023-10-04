def bowling():
    x,p=[0 for _ in range(20)],0
    for _ in range(10):
        x[p]=(int(input()))
        if(p%2==0 and x[p]==10):
            p+=1
        elif(p%2==0 and x[p]<10):
            p+=1
            x[p]=(int(input()))
        p+=1
    
    if(x[-2]==10):
        x.append(int(input()))
        x.append(int(input()))
    if(x[-1]+x[-2]==10):
        x.append(int(input()))
    
    ans=sum(x)

    for i in range(0,18,2):
        if(x[i]==10):
            ans+=x[i+2]+x[i+3]
        elif(x[i]+x[i+1]==10):
            ans+=x[i+2]
    
    return ans

if __name__=='__main__':
    print(bowling())