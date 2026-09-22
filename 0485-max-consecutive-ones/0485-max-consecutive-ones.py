class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                if count>max:
                    max=count
            else:
                count=0
        return max
        