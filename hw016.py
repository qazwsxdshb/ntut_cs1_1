
def getTriangle(ans: list):
    tmp=(sum(ans)*(sum(ans)-ans[0])*(sum(ans)-ans[1])*(sum(ans)-ans[2]))**0.5
    ans=sorted(ans)[-1::-1]
    if(ans[0]>=ans[1]+ans[2] or ans[2]<=0 or ans[1]<=0 or ans[0]<=0):return "not a triangle"
    elif(ans[0]==ans[1] and ans[0]==ans[2] and ans[1]==ans[2]):return "equilateral triangle",tmp
    elif(ans[1]==ans[2] or ans[1]==ans[0] or ans[2]==ans[0]):return "isosceles triangle",tmp
    elif((ans[0]**2)==(ans[1]**2+ans[2]**2)):return "right triangle",tmp
    elif((ans[0]**2)>(ans[1]**2+ans[2]**2)):return "obtuse triangle",tmp
    elif((ans[0]**2)<(ans[1]**2+ans[2]**2)):return "acute triangle",tmp

ans=[]
for _ in range(int(input())):
    ans.append([int(i) for i in input().split()])
for i in range(len(ans)):
    tmp=getTriangle(ans[i])
    if(tmp[1] is not None):
        print(tmp[0],tmp[1])
    else:
        print(tmp[0])