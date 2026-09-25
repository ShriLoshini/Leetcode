class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num=0
        for i in digits:
            num=num*10+i
        num+=1
        ans=[]
        n=str(num)
        for i in n:
            ans.append(int(i))
        return ans
        