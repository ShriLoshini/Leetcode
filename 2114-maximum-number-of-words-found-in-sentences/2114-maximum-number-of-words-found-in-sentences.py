class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max=0
        for i in sentences:
            words=i.split()
            count=len(words)
            if count>max:
                max=count
        return max