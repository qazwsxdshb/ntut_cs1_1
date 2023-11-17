class coverage():
    def __init__(self):
        self.Truecount=0
        self.Falsecount=0
    def Equal(self,test,ans):
        if(test==ans):
            self.Truecount+=1
        else:
            self.Falsecount+=1
    def ans(self):
        print("True:",self.Truecount," False:",self.Falsecount," Cover:",100*self.Truecount/(self.Truecount+self.Falsecount),"%",sep="")