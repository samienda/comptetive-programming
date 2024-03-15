class Solution:
    def mySqrt(self, x: int) -> int:

        low = 1
        high = x

        while high - low > 1:
            mid = (low + high) // 2

            trial = mid ** 2

            if trial > x:
                high = mid
            elif trial < x:
                low = mid
            else: 
                return mid

        return low if x != 0 else 0

        
        