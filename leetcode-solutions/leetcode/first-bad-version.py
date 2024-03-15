# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n

        while left + 1 < right:

            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid

            # print(left, right)
        return left if isBadVersion(left) else right
        