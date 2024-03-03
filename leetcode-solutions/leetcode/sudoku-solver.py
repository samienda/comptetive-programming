class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        empty = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    row[i].add(int(board[i][j])) 
                    col[j].add(int(board[i][j])) 
                    box[(i // 3, j // 3 )].add(int(board[i][j]))
                else:
                    empty.append((i, j))

        canbe = defaultdict(list)
        for i, j in empty:
            for x in range(1, 10):
                if x not in row[i] and x not in col[j] and x not in box[(i//3, j//3)]:
                    canbe[(i, j)].append(x)

        res = []
        _max = 0
        def pick(curr, idx):
            nonlocal empty, canbe, row, col, box, res

            if idx >= len(empty):
                res.append(copy.deepcopy(curr))
                return 
               
               
            for num in canbe[empty[idx]]:
                i, j = empty[idx]
                

                if num in row[i] or num in col[j] or num in box[(i//3, j//3)]:
                    continue 

                found = True
                curr[empty[idx]] = num
                row[i].add(num)         
                col[j].add(num) 
                box[(i // 3, j // 3 )].add(num)
                
               
                pick(curr, idx + 1)

                curr.pop(empty[idx])
                row[i].remove(num)         
                col[j].remove(num) 
                box[(i // 3, j // 3 )].remove(num)
               

        pick({}, 0)
            
        for key, value in res[0].items():
            i, j = key
            board[i][j] = str(value)   
        



            
        