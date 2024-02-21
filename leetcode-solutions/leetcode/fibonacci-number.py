class Solution:
    def fib(self, n: int) -> int:
        # memo = {}
        # def fibo(n):
        #     if n in memo:
        #         return memo[n]

        #     if n == 1:
        #         return 1

        #     if n == 0:
        #         return 0

        #     memo[n - 1] = fibo(n - 1)
        #     memo[n - 2] = fibo(n - 2)
        #     return memo[n - 1] + memo[n - 2]

        # return fibo(n)
        
        a = 0
        b = 1

        for _ in range(n - 1):
            a, b = b, a + b

        return b if n != 0 else a