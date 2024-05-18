# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        def inbound(i, j):return 0 <= i < n and 0 <= j < m

        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):

                if obstacleGrid[i][j] == 0:

                    if inbound(i + 1, j):
                        dp[i + 1][j] += dp[i][j]
                        
                    if inbound(i, j + 1):
                        dp[i][j + 1] += dp[i][j]


        return dp[-1][-1] if obstacleGrid[-1][-1] == 0 else 0