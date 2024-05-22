# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        matrix[-1] = [int(i) for i in matrix[-1]]

        for i in range(n - 2, -1, -1):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    matrix[i][j] += int(matrix[i + 1][j])

        # print(matrix)
        maximum = 0
        for i in range(n):
            for j in range(m):
                target = 0
                
                mini = matrix[i][j]
                for k in range(j, m):
                    if target + 1 > matrix[i][k] or mini <= target:
                        break

                    mini = min(mini, matrix[i][k])
                    target += 1
                maximum = max(maximum, target)
                # print(target, j)
            # print(i, matrix[i], maximum)
        return maximum ** 2
