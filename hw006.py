ans=[]
for i in input().split():ans.append(int(i))
ans=sorted(ans)[-1::-1]
if(ans[0]>sum(ans[1:])):print("not triangle")
elif(ans[0]==ans[1] and ans[0]==ans[2]):print("equilateral triangle")
elif(ans[1]==ans[2] or ans[1]==ans[0]):print("isosceles triangle")
else:print("triangle")