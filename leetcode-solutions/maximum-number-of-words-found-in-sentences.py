class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        lis = [len(list(word.split())) for word in sentences] 
        
        lis.sort()
        return lis.pop()