class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    


        def pascal(lis, n):
            if n <= 0:
                return lis

            newlis = [1]
            for i in range(1, len(lis)):
                newlis.append(lis[i] + lis[i - 1])

            newlis.append(1)

            return pascal(newlis, n - 1)


        return pascal([1], rowIndex)