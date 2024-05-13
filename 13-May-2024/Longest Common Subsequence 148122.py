# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        memo = {}
        def take(i, j):
            if i >= n or j >= m:return 0

            state = (i, j)
            if state not in memo:
                if text1[i] == text2[j]:
                    memo[state] = take(i + 1, j + 1) + 1
                else:
                    memo[state] = max(take(i + 1, j), take(i, j + 1))
            
            return memo[state]
        
        return take(0, 0)
