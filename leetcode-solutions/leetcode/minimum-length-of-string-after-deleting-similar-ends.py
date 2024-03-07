class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        left = 0
        right = n - 1

        while left < right:
            # print(left, right)
            if s[left] == s[right]:

                while left < right and s[left + 1] == s[right]:
                    left += 1
                    
                while left < right and s[left] == s[right - 1]:
                    right -= 1
            else:
                break
            left += 1
            right -= 1
        
        return max(right - left + 1, 0)