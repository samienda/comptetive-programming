class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        res = [[] for _ in range(m)]
        
        for i in range(n):
            for j in range(m):
                res[j].append(matrix[i][j])

        return res

     

        