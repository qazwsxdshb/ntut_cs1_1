def player():
    return [input() for _ in range(4)]
def calc(tmp: int,ans=0):
    for i in range(1,len(tmp)):
        if(tmp[i][0].isalpha()):
            ans+=0.5
        else:
            ans+=int(tmp[i][0])
    return ans

if __name__=="__main__":
    a=player()
    b=player()
    x=float('%1f' %calc(a))
    if(x>10.5):
        x=0
    y=float('%1f' %calc(b))
    if(y>10.5):
        y=0
    
    if(int(x)<=0):
        print(b[0],"Win")
    elif(y<x):
        print(a[0],"Win")
    elif(x<y):
        print(b[0],"Win")
    else:
        print("Tie")

    if(y<x):
        print(a[0],"Win")
    elif(x<y):
        print(b[0],"Win")
    else:
        print("Tie")