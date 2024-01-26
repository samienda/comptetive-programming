class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        need = Counter(t)
        have = Counter()
        k = len(need)
        count = n + 1
        res = ""
        check = set()

        left = 0
        for right in range(n):
            have[s[right]] += 1

            if s[right] in need and s[right] not in check and have[s[right]] >= need[s[right]]:
                check.add(s[right])
                k -= 1

            while k <= 0:
                if count > right - left + 1:
                    count =  right - left + 1
                    res = s[left: right + 1]
                
                have[s[left]] -= 1
                if s[left] in need and s[left] in check and have[s[left]] < need[s[left]]:
                    k += 1
                    check.remove(s[left])



                left += 1 

        
        return res
        