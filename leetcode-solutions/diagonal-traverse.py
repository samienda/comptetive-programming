class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])


        i, j = 0, 0
        up = True
        res = [mat[0][0]]
        while i < n and j < m:
            if up:
                if j + 1 < m:
                    j += 1
                else:
                    i += 1
                up = False
            else:
                if i + 1 < n:
                    i += 1
                else:
                    j += 1
                up = True

            if i < n and j < m:
                res.append(mat[i][j])
            
            while up and i - 1 >= 0 and j + 1 < m:
                i -= 1
                j += 1
                res.append(mat[i][j]) 

            while not up and j - 1 >= 0 and i + 1 < n: 
                i += 1
                j -= 1
                res.append(mat[i][j]) 

        return res


            