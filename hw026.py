class Solution:
    def __init__(self,person,day,first_positive,spread,recovery_day,immunity):
        self.person,self.day,self.first_positive,self.spread,self.recovery_day,self.immunity=person,day,first_positive,spread,recovery_day,immunity
    
    def ans(self):
        tmp_day=[0]*(self.recovery_day)
        tmp_day.append(self.first_positive)
        total=self.first_positive
        for i in range(1,1+self.day):
            tmp=tmp_day.pop(0)
            x=self.positive_person(total)*int(sum(tmp_day)) if i!=1 else 0
            print(self.positive_person(total))
            total+=x
            tmp_day.append(x)
            print(i,int(sum(tmp_day)),int(self.first_positive) if i==1 else int(x),int(tmp))
    
    def positive_person(self,recovery_person):
        return (self.spread/self.recovery_day)*(1-self.immunity-recovery_person/self.person)

if(__name__=="__main__"):
    ans=Solution(int(input()),int(input()),int(input()),float(input()),int(input()),float(input()))
    ans.ans()