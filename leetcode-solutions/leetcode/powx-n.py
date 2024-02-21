class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        if n < -300 and not (-2 < x < 2):
            return 0

        if x == 1:
            return 1
        def power(n):
            
            if n == 0:
                return 1

            if n == 1:
                return x

            if n < 0:
                return 1/ power(abs(n))

            if n % 2 == 0:
                return power(n//2) **2
            else:
                return power(n - 1) * x 
        

        return power(n)