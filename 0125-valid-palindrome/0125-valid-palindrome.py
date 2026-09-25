class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new=""
        for i in s:
            if i.isalnum():
                new=new+i
        n=new[::-1]
        return new==n

        