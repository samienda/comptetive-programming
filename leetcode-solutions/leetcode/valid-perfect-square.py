class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True


        low = 1
        high = num

        while low <= high:

            mid = (low + high) // 2

            if mid ** 2 > num:
                high = mid - 1
            elif mid ** 2 < num:
                low = mid + 1
            else:
                return True

        return False
        