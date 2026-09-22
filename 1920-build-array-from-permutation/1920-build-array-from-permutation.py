class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        for i in range (n):
            a=nums[nums[i]]
            ans.append(a)
        return ans
        