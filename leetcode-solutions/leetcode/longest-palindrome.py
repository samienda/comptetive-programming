class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
    
        
        total = 0
        found = False
        for key, value in count.items():
            total +=  value

            if value % 2 != 0:
                found = True
                total -= 1

        return total if not found else total + 1

            

