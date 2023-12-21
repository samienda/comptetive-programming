class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from copy import deepcopy
        n = len(matrix)

        temp = [[0, 0], [n-1, 0], [n -1, n- 1], [0, n- 1]]
        updatein = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        updateout = [[1, 1], [-1, 1], [-1, -1], [1, -1]]


        for _ in range(n//2):
            direction = deepcopy(temp)
            
            while direction[0][1] < direction[3][1]:
                for i in range(3):

                    start = matrix[direction[i][0]][direction[i][1]]
                    end = matrix[direction[i + 1][0]][direction[i + 1][1]]
                   
                 
                    matrix[direction[i][0]][direction[i][1]] = end
                    matrix[direction[i + 1][0]][direction[i + 1][1]] = start

                    start2 = matrix[direction[i][0]][direction[i][1]]
                    end2 = matrix[direction[i + 1][0]][direction[i + 1][1]]
                   
                for j in range(4):
                    direction[j][0] += updatein[j][0] 
                    direction[j][1] += updatein[j][1]
                

        
            for k in range(4):
                temp[k][0] += updateout[k][0]    
                temp[k][1] += updateout[k][1]
            

            