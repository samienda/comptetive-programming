class Solution:
    def largestOddNumber(self, num: str) -> str:
        

        n = len(num)

        maximum_odd = ''

        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                maximum_odd = num[:i + 1]
                break

        return maximum_odd