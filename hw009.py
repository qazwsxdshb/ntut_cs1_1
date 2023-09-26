s=[int(input()) for _ in range(6)]
ans=0
for i in range(0,len(s),2):
    ans+=abs(s[i]-s[i+1])

if(s[1]>s[2]):
    if(s[3]<s[1]):
        ans-=abs(s[2]-s[3])
    else:
        ans=ans-abs((s[1])-s[2])
if(s[3]>s[4]):
    if(s[5]<s[3]):
        ans-=abs(s[5]-s[4])
    else:
        ans=ans-abs((s[3])-s[4])
if(s[1]>s[4]):
    if(s[5]<s[1]):
        ans-=abs(s[5]-s[4])
    else:
        ans=ans-abs((s[1])-s[4])
print(abs(ans))