# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def ispalindrome(s):
            right = len(s) - 1
            for left in range(len(s)//2):
                if s[left] != s[right]:return False
                right -= 1

            return True
        # print(ispalindrome("abba"))
        answer = []
        # @cache
        def pick(idx, curr, lis):
            if idx >= len(s):
                # print(curr, lis)
                if ispalindrome(curr):
                    lis += (curr,)
                    answer.append(lis)
                # print(lis)
                return

            if ispalindrome(curr):
                pick(idx + 1, s[idx], lis + (curr,))
            pick(idx + 1, curr + s[idx], lis)

        pick(1, s[0], ())
        return answer
