class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        
        s = list(s)

        right = 0
        swap = 0

        for left in range(n):
            if s[left] == '1':
                if right <= left:
                    right = left + 1
                
                while right < n and s[right] != '0':
                    right += 1

                if right < n:
                    s[left], s[right] = s[right], s[left]
                    swap += right - left
                    right += 1

        return swap



