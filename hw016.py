
def getTriangle(ans: list):
    s=sum(ans)/2
    tmp=(s*(s-ans[0])*(s-ans[1])*(s-ans[2]))**0.5
    ans=sorted(ans)[-1::-1]
    if(ans[0]>=ans[1]+ans[2] or ans[2]<=0 or ans[1]<=0 or ans[0]<=0):return "not a triangle","no"
    elif(ans[0]==ans[1] and ans[0]==ans[2] and ans[1]==ans[2]):return "equilateral triangle",tmp
    elif(ans[1]==ans[2] or ans[1]==ans[0] or ans[2]==ans[0]):return "isosceles triangle",tmp
    elif((ans[0]**2)==(ans[1]**2+ans[2]**2)):return "right triangle",tmp
    elif((ans[0]**2)>(ans[1]**2+ans[2]**2)):return "obtuse triangle",tmp
    elif((ans[0]**2)<(ans[1]**2+ans[2]**2)):return "acute triangle",tmp

ans=[]
for _ in range(int(input())):
    ans.append([int(i) for i in input().split()])
t=[]
for i in range(len(ans)):
    tmp,a=getTriangle(ans[i])
    if(a != "no"):
        t.append("%.2f" %a)
        print(tmp,"%.2f" %a)
    else:
        print(tmp)
if(len(t)==0):
    print("All inputs are not triangles!")
else:
    print(max(t))
    print(min(t))