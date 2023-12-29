class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split()
        n = len(splitted)

        idx_word = []
        for word in splitted:
            m = len(word)
            idx_word.append([int(word[m-1]), word[:m-1]])


        idx_word.sort()


        res = ""
        for word in idx_word:
            res += word[1] + " "

        return res.strip()
        
        