# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        

        @cache
        def pick(x):
            # if sum(nums) == n:
            #     print(nums)

            found = 1
            for i in range(1, x):

                found = max(found, pick(x - i) * i)

            return found

        return pick(n + 1)