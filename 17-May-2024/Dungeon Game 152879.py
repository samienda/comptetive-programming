# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n, m = len(dungeon), len(dungeon[0])
        def inbound(row, col): return 0 <= row < n and 0 <= col < m
        
        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):

                val = float('-inf') if row != n - 1 or col != m - 1 else 0
                if inbound(row + 1, col):
                    val = max(val, dungeon[row + 1][col])
                if inbound(row, col + 1):
                    val = max(val, dungeon[row][col + 1])

                dungeon[row][col] += val
                if dungeon[row][col] > 0:
                    dungeon[row][col] = 0
                


        # print(dungeon)
        return -dungeon[0][0] + 1