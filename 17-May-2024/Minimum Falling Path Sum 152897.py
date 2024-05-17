# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n, m = len(matrix), len(matrix[0])
        
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m


        for row in range(n - 2, -1, -1):
            for col in range(m):
                
                val = float('inf')
                if inbound(row + 1, col - 1):
                    val = min(val, matrix[row + 1][col - 1])

                if inbound(row + 1, col ):
                    val = min(val, matrix[row + 1][col])

                if inbound(row + 1, col + 1):
                    val = min(val, matrix[row + 1][col + 1])

                matrix[row][col] += val
            
            
        
        return min(matrix[0])
