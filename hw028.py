class Sloution:
    def __init__(self,start,end,rep,ace):
        self.string,self.rep,self.ace=start+" "+end,rep,ace
    def ans(self):
        return self.string
    def rep_ans(self,x):
        self.tmp=""
        for i in self.string.split():self.tmp+= self.ace[::x]+" " if(" "+self.rep.lower()+" "==" "+i.lower()+" ") else i+" "
        return self.tmp[:-1]
    def spi_ans(self):
        return self.string[::abs(len(self.rep)-len(self.ace))]
if __name__=="__main__":
    ans=Sloution(input(),input(),input(),input())
    print(ans.ans(),"\n",ans.rep_ans(1),"\n",len(ans.ans().replace(" ",""))," ",len(ans.rep_ans(1).replace(" ","")),"\n",ans.rep_ans(-1),"\n",ans.spi_ans().replace("  "," "),sep="")