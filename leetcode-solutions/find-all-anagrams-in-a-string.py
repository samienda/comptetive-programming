class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)

        w = s[:m] 

        pcount = Counter(p)
        scount = Counter(w)
        res = []

        if pcount == scount:
            res.append(0)


        for i in range(m,n):
            scount[s[i]] += 1
            scount[s[i - m]] -= 1
            if pcount == scount:
                res.append(i +  1 - m)


        return res






        

