class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def divide(s):
            if not s:
                return s

            unique = set(s)
            x = len(s) // 2
            for i in range(len(s)):

                if s[i].upper() not in unique or s[i].lower() not in unique:
                    x = i
                    break
            else:
                return s
            
            left =  divide(s[:i])
            right =  divide(s[i + 1:])
            
            return left if len(left) >= len(right) else right
            
        return divide(s)

        