class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        prefix = [0] * n
        suffix = [0] * n
        
        running = 0
        for i in range(n - 1):
            if s[i] == '0':
                prefix[i] += 1


            running += prefix[i]
            prefix[i] = running

            
        running = 0
        for i in range(n- 1, 0, -1):
            if s[i] == '1':
                suffix[i] += 1


            running += suffix[i]
            suffix[i] = running

        print(prefix, suffix)
        # prefix[0], suffix[n - 1] = 0, 0
        ans = [prefix[i] + suffix[i + 1] for i in range(n - 1)]
        return max(ans)

