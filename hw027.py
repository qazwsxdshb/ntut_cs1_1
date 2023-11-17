class Solution:
    def __init__(self,deep):
        self.deep,self.stack,self.tmp=deep,[],[]
        for _ in range(6):self.tmp.append([])
    def ans(self,string):
        try:
            tmp,ans=-1,""
            for i in string:
                if(i in "([{"):
                    tmp+=1
                    self.stack.append(i)
                elif(i in "}])"):
                    tmp-=1
                    x=self.stack.pop()
                    if((i==")" and ord(x)==40) or (i=="]" and ord(x)==91) or (i=="}" and ord(x)==123)):pass
                    else:return "fail"
                else:self.tmp[tmp].append(i)
            if(len(self.stack)!=0):return "fail"
            for i in self.tmp[self.deep-1]:ans+=i
            return ans
        except:return "fail"
if(__name__=="__main__"):
    x,deep=int(input()),int(input())
    for i in range(x):
        ans=Solution(deep)
        x=ans.ans(input())
        if(x!="fail"):print("pass, ", x if len(x)!=0 else "EMPTY",sep="")
        else:print(x)