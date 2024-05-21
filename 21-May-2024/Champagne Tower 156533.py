# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        dp = [[0 for j in range(100)]  for i in range(101)]

        dp[0][0] = poured


        col = 1
        for i in range(99):
            for j in range(col):
                if dp[i][j] > 1:
                    dp[i + 1][j] += (dp[i][j] - 1) / 2
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2


            col += 1

        # print(dp[query_row])
        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1 else 1