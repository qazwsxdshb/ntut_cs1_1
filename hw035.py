class solve:
    def __init__(self,university,type) -> None:
        self.type=type
        self.university=university
    
    def main(self,seq):
        if(self.type=="0"):
            return self.type_0(seq,[])
        elif(self.type=="1"):
            return self.type_1(seq,[])
        
    def type_0(self,seq,ans=[]):
        for i in seq:
            for u in self.university.items():
                if(all(c in list(u)[1] for c in i)):
                    ans.append(u[0])
        return set(ans)
    
    def type_1(self,seq,ans=[]):
        tmp=[]
        for i in seq:
            for u in i:
                tmp.append(u)
        for u in self.university.items():
            a=list(filter(lambda x: x in list(u)[1],tmp))
            ans.append([u[0],len(a)])
        tmp=[]
        for i in ans:
            if(i[1]==max(ans,key=lambda x: x[1])[1]):tmp.append(i[0])
        return tmp
                
university,seq={},[]
for _ in range(int(input())):
    tmp=input().split()
    university[tmp[0]]=tmp[1:]

for _ in range(int(input())):
    tmp,tmp2=[],[]
    for i in input().split():
        if(i=="+"):
            tmp2.append(tmp)
            tmp=[]
        else:tmp.append(i)
    seq.append(tmp2+[tmp])

ans=solve(university,input())
for i in seq:
    fin_fin_ans=[]
    x=ans.main(i)
    for i in university.items():
        if(i[0] in x):fin_fin_ans.append(i[0])
    print(*fin_fin_ans)