class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        result = []
        for i in range(n):

            res = []
            for j in range(n - 1 , -1, -1):

                img = image[i][j]
                
                if img == 1:
                    res.append(0)
                else:
                    res.append(1)

            result.append(res)

        return result