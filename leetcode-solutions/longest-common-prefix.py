class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lp = ''
        flag = True
        mini = min(len(s) for s in strs)
       
        for i in range(mini):
            for s in strs:
                if strs[0][i] != s[i]:
                    return lp
            lp = lp + strs[0][i]

        return lp 

