class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        n = len(d)
        x = n - 1


        num = 0
        for i in range(n):
            num += d[i]* (10**x)
            x -= 1


        num += 1
        num = str(num)

        x = 0
        res = []
        for j in range(len(num)):
            res.append(int(num[j]))


        return res





            