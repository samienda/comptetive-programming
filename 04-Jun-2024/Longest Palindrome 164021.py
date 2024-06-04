# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        odd = 1
        total = 0
        for val in count.values():
            if val % 2:
                total += val - 1
                if odd > 0:
                    total += 1
                    odd -= 1
            else:
                total += val

        return total

        