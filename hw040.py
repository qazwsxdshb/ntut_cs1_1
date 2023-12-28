prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
start,end,DNA,ans=input(),input().split(),input(),[]
for i in range(len(DNA)-len(start)+1):
    if(DNA[i:i+len(start)]==start):
        tmp=""
        for u in range(i+len(start),len(DNA)):
            if(DNA[u:u+len(end)] in end and len(tmp) in prime):
                ans.append(tmp)
                break
            else:tmp+=DNA[u]
for i in (sorted(ans,key=lambda x:(len(x),x))):print(i)
if(len(ans)==0):print("No gene")