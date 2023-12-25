class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)


        direction = [[0, 0], [n - 1, 0]]

        curr = 0
        while direction[0][0] < n:
            curr += mat[direction[0][0]][direction[0][1]]
            curr += mat[direction[1][0]][direction[1][1]]

            direction[0][0] += 1
            direction[0][1] += 1


            direction[1][0] -= 1
            direction[1][1] += 1

        if n % 2 != 0:
            return curr - mat[n//2][n//2]

        return curr


        