class Solution:
    def pivotInteger(self, n: int) -> int:

        def pivot(left, right, n):
            if left == right + n:
                return n

            if n == 0:
                return -1

            return pivot(left - n, right + n, n - 1)

        return pivot((n + 1) * (n / 2), 0, n)
        