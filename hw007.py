ans=[]
for i in input().split():ans.append(int(i))
ans_sum=sum(ans)/len(ans)
ans_ch=0
for i in ans:
    ans_ch+=(i-ans_sum)**2
print("%.2f" %(ans_ch/len(ans)),"\n","%.2f" %((ans_ch/len(ans))**0.5),"\n","%.2f" %ans_sum,sep="")