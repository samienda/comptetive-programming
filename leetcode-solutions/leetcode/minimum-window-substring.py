class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        need = Counter(t)
        have = Counter()
        k = len(need)
        count = n + 1
        res = [-1, -1]
        check = set()

        left = 0
        for right in range(n):
            have[s[right]] += 1

            if s[right] in need and have[s[right]] == need[s[right]]:
                k -= 1

            while k <= 0:
                if count > right - left + 1:
                    count =  right - left + 1
                    res = [left, right + 1]
                
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    k += 1
                    


                left += 1 

        
        return s[res[0]: res[1]]
        