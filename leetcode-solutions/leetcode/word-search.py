class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        m, n = len(board), len(board[0])
        final = False
        def pick(curr, row, col, seen):
            nonlocal final, n, m
            # pruning case 2
            if final:
                return 
            x = len(curr)

            # pruning case 1
            if curr and curr[-1] != word[x - 1]:
                return

            if x == len(word):
                if curr == word:
                    final = True
                return 

            # base case
            if not (0 <= row < m and 0 <= col < n):
                return 
            # print(curr, row, col, seen)
            
            if (row, col) in seen:
                return
            seen.add((row, col))
            # right
            pick(curr + board[row][col], row, col + 1, seen ) 
        
            # down
            pick(curr + board[row][col], row + 1, col, seen ) 
            
            # left
            pick(curr + board[row][col], row, col - 1, seen) 
            
            # up
            pick(curr + board[row][col], row - 1, col, seen)

            seen.remove((row, col))


        for row in range(m):
            for col in range(n):
                if not final and board[row][col] == word[0]:
                    pick("", row, col, set())
        return final
         

            