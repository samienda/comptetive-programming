class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ ['.'] * n for _ in range(n)]
        row = defaultdict(set)
        col = defaultdict(set)
        posdiagonal = defaultdict(set)
        negdiagonal = defaultdict(set)

        res = set()
        def pick(curr, idx, x):
            nonlocal res, row, col, posdiagonal, negdiagonal
            
            if idx >= n:
                res.add(tuple(sorted(curr)))
                return

            for i in range(x, n):
                for j in range(n):

                    if row[i] or col[j] or posdiagonal[i - j] or negdiagonal[i + j]:
                        continue

                    curr.add((i, j))
                    row[i].add('q') 
                    col[j].add('q') 
                    posdiagonal[i - j].add('q') 
                    negdiagonal[i + j].add('q') 

                    pick(curr, idx + 1, i + 1)
                    
                    curr.remove((i, j))
                    row[i].remove('q') 
                    col[j].remove('q') 
                    posdiagonal[i - j].remove('q') 
                    negdiagonal[i + j].remove('q') 
        
        pick(set(), 0, 0)
        # return [[""]]
        
        ans = []
        original = copy.deepcopy(board)
        
        for item in res:
            board = copy.deepcopy(original)
            currboard = []
            for i, j in item:
 
                board[i][j] = 'Q'
                x = "".join(board[i])
                
                currboard.append(copy.deepcopy(x))

            ans.append(currboard)

        return ans
