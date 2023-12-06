class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])


        visted = [(0, 0), (-1, 0), (0, -1), (n, m - 1), (n - 1, m), (-1, m -1), (0, m)]
       
        row = column = 0
        res=[matrix[0][0]]

        while len(res) < n * m:
           
            while (row , column + 1) not in visted and 0 <= row < n and 0 <= column + 1 < m:
                column += 1

                visted.append((row, column))
                res.append(matrix[row][column])


            while (row + 1, column) not in visted and 0 <= row  + 1< n and 0 <= column < m:
                row += 1

                visted.append((row, column))
                res.append(matrix[row][column])


            while (row , column - 1) not in visted and 0 <= row < n and 0 <= column - 1 < m:
                column -= 1

                visted.append((row, column))
                res.append(matrix[row][column])
            
            
            while (row - 1 , column) not in visted and 0 <= row  - 1< n and 0 <= column < m:
                row -= 1
                
                visted.append((row, column))
                res.append(matrix[row][column])


        return res





