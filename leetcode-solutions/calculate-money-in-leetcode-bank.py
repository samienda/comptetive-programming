class Solution:
    def totalMoney(self, n: int) -> int:
        
        count = 0
        result = 0

        for i in range(1, n + 1):
            result += (i % 7) + count

            if i % 7 == 0:
                count += 1
                result += 7


        return result
