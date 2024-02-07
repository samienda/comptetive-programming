class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])

        mat = []
        mat.append([0] * (m + 1))

        for _ in range(n):
            mat.append([0] + matrix[_])
        
        from copy import deepcopy
        self.prefix = deepcopy(mat)
        self.mat = mat


        for row in range(1, n + 1):
            for col in range(1, m+ 1):
                self.prefix[row][col] = self.prefix[row - 1][col] + self.prefix[row][col - 1] + self.prefix[row][col] - self.prefix[row-1][col- 1]

        print(self.mat) 
        print(self.prefix) 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] -  self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1] 

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)