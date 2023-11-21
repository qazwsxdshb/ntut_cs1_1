ans=0
for i in range(int(input())):
    tmp=list(map(float,input().split()))
    ans+=tmp[0]*tmp[1]
print(int(((1-int(input())/30)+ans*0.001)*100//1),"%",sep="")