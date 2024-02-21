class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def power(x, n):
            
            if n == 0:
                return 1

            if n == 1:
                return x


            if n % 2 == 0:
                return (power(x, n//2) **2) % mod
            else:
                return (power(x, n - 1) * x) % mod 
        

        q = n // 2
        r = n % 2

        return (power(4, q) * power(5, q + r)) % mod

 
        