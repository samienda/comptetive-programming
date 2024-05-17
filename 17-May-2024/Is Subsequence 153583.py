# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]


        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(
                        dp[row][col - 1],
                        dp[row - 1][col]   
                    )
        # print()
        return dp[-1][-1] == n