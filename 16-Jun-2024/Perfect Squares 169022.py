# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        

        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0

        for i in range(n):

            for j in range(1, int(n**0.5) + 1):
                idx = i + (j ** 2)
    
                if idx <= n:
                    dp[idx] = min(dp[idx], dp[i] + 1)


        return dp[-1]

