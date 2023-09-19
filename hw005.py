def getTriangle(ans: list): 
    ans=sorted(ans)[-1::-1]
    if(ans[0]>=ans[1]+ans[2] or ans[2]<=0 or ans[1]<=0 or ans[0]<=0):return "not a triangle"
    elif(ans[0]==ans[1] and ans[0]==ans[2] and ans[1]==ans[2]):return "equilateral triangle"
    elif(ans[1]==ans[2] or ans[1]==ans[0] or ans[2]==ans[0]):return "isosceles triangle"
    elif((ans[0]**2)==(ans[1]**2+ans[2]**2)):return "right triangle"
    elif((ans[0]**2)>(ans[1]**2+ans[2]**2)):return "obtuse triangle"
    elif((ans[0]**2)<(ans[1]**2+ans[2]**2)):return "acute triangle"
print(getTriangle([int(input()) for _ in range(3)]))