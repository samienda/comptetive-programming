# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        row = n - 1
        for i in range(n - 2, -1, -1):
            for j in range(row):
                # print(i, j)
                triangle[i][j] += min(
                    triangle[i + 1][j],
                    triangle[i + 1][j + 1]
                )

            row -= 1

        return min(triangle[0])
