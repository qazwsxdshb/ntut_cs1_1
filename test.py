class Solution:
    def __init__(self,number) -> None:
        self.stack=[0]*number
        self.top=-1
    def push(self,ans):
        self.top+=1
        self.stack[self.top]=ans
    def pop(self):
        x=self.top
        self.top-=1
        self.stack.append(0)
        return x,self.stack.pop(x)
    def pr_stack(self):
        return self.stack

stack=Solution(10)

stack.push('a')
stack.push('b')
stack.push('c')
stack.push('d')
top,y = stack.pop()
print(y,top)
stack.push('f')
stack.push('g')
top,y =  stack.pop()
print(y,top)
top,y =  stack.pop()
print(y,top)
top,y =  stack.pop()
print(y,top)

print(stack.pr_stack())


# 1.由左至右依序讀取字串
# 2.讀取到左括號時將其push至stack中
# 3.取到右括號時將stack中最上方的資料pop出來比對是否對應
# 4.若無法對應，輸出無法對應。
# 5.直至整個讀取完成後查看stack是否有值。