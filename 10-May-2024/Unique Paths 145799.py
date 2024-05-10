# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        
        def inbound(row, col):return 0 <= row < n and 0 <= col < m
        def evaluate(row, col):return row == n - 1 and col == m - 1

        memo = {}
        def move(row, col):
            if not inbound(row, col):return 0
            if evaluate(row, col):return 1

            state = (row, col)
            if state not in memo:
                memo[state] = move(row + 1, col) + move(row, col + 1)

            return memo[state]

        return move(0, 0)