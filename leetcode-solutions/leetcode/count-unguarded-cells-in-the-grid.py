class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        

        grid = [['.'] * m for _ in range(n)]


        for row, col in walls:
            grid[row][col] = 'w'

        # print(grid)

        for row, col in guards:
            grid[row][col] = 'g'

        count = 0
        curr = 0
        stack1 = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    curr += 1
                    stack1.append((i, j))
                elif grid[i][j] == 'g':
                    while curr and stack1:
                        stack1.pop()
                        curr -= 1
                else:
                    count += curr
                    curr = 0
            count += curr
            curr = 0
            
        # print(stack1)
       
        count = 0
        curr = 0
        stack2 = []
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == '.':
                    curr += 1
                    stack2.append((i, j))
                elif grid[i][j] == 'g':
                    while curr and stack2:
                        stack2.pop()
                        curr -= 1
                else:
                    count += curr
                    curr = 0
            count += curr
            curr = 0

        # print(stack2)
       
        count = 0
        curr = 0
        stack3 = []
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[j][i] == '.':
                    curr += 1
                    stack3.append((j, i))
                elif grid[j][i] == 'g':
                    while curr and stack3:
                        stack3.pop()
                        curr -= 1
                else:
                    count += curr
                    curr = 0
            count += curr
            curr = 0

        # print(stack3)
       
        count = 0
        curr = 0
        stack4 = []
        for i in range(m):
            for j in range(n):
                if grid[j][i] == '.':
                    curr += 1
                    stack4.append((j, i))
                elif grid[j][i] == 'g':
                    while curr and stack4:
                        stack4.pop()
                        curr -= 1
                else:
                    count += curr
                    curr = 0
            count += curr
            curr = 0

        # print(stack4)

        # stack1 = set(stack1
        stack2 = set(stack2)
        stack3 = set(stack3)
        stack4 = set(stack4)

        count = 0
        for item in stack1:
            if item in stack2 and item in stack3 and item in stack4:
                count += 1

        return count






            # # up
            # x, y = row, col
            # while x + 1 < n and grid[x + 1][y] != 'w':
            #     x += 1
            #     grid[x][y] = 'c'
                
            # # down
            # x, y = row, col
            # while 0 <= x - 1 and grid[x - 1][y] != 'w':
            #     x -= 1
            #     grid[x][y] = 'c'

                
            # # right
            # x, y = row, col
            # while y + 1 < m and grid[x][y + 1] != 'w':
            #     y += 1
            #     grid[x][y] = 'c'

            # # left
            # x, y = row, col
            # while 0 <= y - 1 and grid[x][y - 1] != 'w':
            #     y -= 1
            #     grid[x][y] = 'c'
        # print("     ")
        # print("     ")
        # print("     ")
        # print(grid)