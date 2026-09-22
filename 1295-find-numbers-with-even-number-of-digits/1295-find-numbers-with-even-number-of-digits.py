class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            a=len(str(nums[i]))
            if a%2==0:
                count+=1
        return count

       

        