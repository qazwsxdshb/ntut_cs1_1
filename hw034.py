class Solution:
    def __init__(self,relationship) -> None:
        self.relationship=relationship
        
    def main(self,start,end):
        ans=self.type_1(start,end,[start],self.relationship)
        print(len(min(ans,key=lambda x:len(x)))-2,"\n"," ".join(min(ans,key=lambda x:len(x))[:-1]),"\n",max(ans,key=lambda x:x[-1])[-1],"\n"," ".join(max(ans,key=lambda x:x[-1])[:-1]),sep="")

    def type_1(self,start,end,ans,relationship,tmp=[],soc=0):
        if(start==end):
            ans.append(soc)
            return [ans]
        if(len(relationship)!=0):
            for i in relationship:
                if(i[0]==start and i[1] not in ans):
                    x=self.type_1(i[1],end,ans+[i[1]],relationship,tmp,soc+min(int(relationship[i][0]),int(relationship[i[1]+i[0]][0])))
                    c=0
                    for i in x:
                        if(i in tmp):
                            c=1
                            break
                    if(c==0):tmp+=x
        return tmp

relationship,_={},input()
while 1:
    x=input().split()
    if(x[0]=="-1"):break
    relationship[x[0]+x[1]]=x[2:]
ans=Solution(relationship).main("A","B")