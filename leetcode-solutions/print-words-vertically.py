class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = list(map(str, s.split()))
        
        m = max([len(st) for st in s])
        n = len(s)
        
        res = ["" for _ in range(m)]
        
        for i in range(n):
            for j in range(m):
        
                if len(s[i]) <= j:
                    res[j] += " "
                else:
                    res[j] += s[i][j]


        return [r.rstrip() for r in res]




        