s=[int(input()) for i in range(6)]
ans=sum(s)
ans=ans-(max(s[:2])-min(s[2:4])) if(max(s[:2])-min(s[2:4]))>0 else ans
ans=ans-(max(s[2:4])-min(s[4:])) if(max(s[2:4])-min(s[4:]))>0 else ans

print("ans:",ans)