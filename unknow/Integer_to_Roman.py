roman={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
class Solution:
    def intToRoman(self, num: int) -> str:
        ans=""
        while num!=0:
            for i,u in reversed(list(roman.items())):
                if(num-u>=0):
                    ans+=i
                    num-=u
                    break
        return ans


ans=Solution()
print(ans.intToRoman(int(input())))