class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = list(palindrome)
        n = len(p)
        odd = False
        if n % 2 != 0:
            odd = True

        for i in range(n):
            if p[i] != 'a':
                if odd and i == (n // 2):
                    continue
                p[i] = 'a'
                break
        else:
            p[n - 1] = 'b'

        return "".join(p) if n > 1 else ""
        
        