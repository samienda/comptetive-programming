class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for num in range(n,2* n + 1, n):
            if num %  2 == 0:
                return num 