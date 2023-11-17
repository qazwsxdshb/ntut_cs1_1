class Solution:
    def __init__(self,person,day,first_positive,spread,recovery_day,immunity):
        self.person,self.day,self.first_positive,self.spread,self.recovery_day,self.immunity=person,day,first_positive,spread,recovery_day,immunity
    
    def ans(self):
        tmp_day=[0]*(self.recovery_day)
        tmp_day.append(self.first_positive)
        total,recover_total=self.first_positive,0
        for i in range(1,1+self.day):
            tmp=tmp_day.pop(0)
            tt=int(sum(tmp_day)+tmp)
            x=int(self.positive_person(recover_total,total,tt)) if i!=1 else 0
            recover_total+=tmp
            total+=x
            tmp_day.append(x) if 1!=i else None
            print(i,int(sum(tmp_day)),int(self.first_positive) if i==1 else int(x),int(tmp))
        print(total)

    def positive_person(self,recovery_person,total,tt):
        tmp=(self.spread/self.recovery_day)*(1-self.immunity-recovery_person/self.person) if int(self.person*self.immunity+total)<self.person else 0
        ans=self.person-int(self.person*self.immunity+total) if int(self.person*self.immunity+total)+int(tmp*tt)>=self.person else tmp*tt
        return ans

if(__name__=="__main__"):
    ans=Solution(int(input()),int(input()),int(input()),float(input()),int(input()),float(input()))
    ans.ans()