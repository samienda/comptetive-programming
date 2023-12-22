class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        def function(x, y):
            res = grid[x + 1][y + 1]
            for i in range(3):
                res += grid[x] [y + i]
                res += grid[x + 2][ y + i]

            return res


        maxi = 0

        for i in range( m - 2):
            for j in range(n - 2):
                maxi = max(maxi, function(i, j))

        return maxi

