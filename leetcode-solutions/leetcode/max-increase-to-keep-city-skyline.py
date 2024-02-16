class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row = defaultdict(int)
        col = defaultdict(int)


        for r in range(n):
            for c in range(n):
                if row[r] < grid[r][c]:
                    row[r] = grid[r][c]

                if col[c] < grid[r][c]:
                    col[c] = grid[r][c]

        # print(row, col)

        total = 0
        for r in range(n):
            for c in range(n):
                total += abs(grid[r][c] - min(row[r], col[c]))

        return total

