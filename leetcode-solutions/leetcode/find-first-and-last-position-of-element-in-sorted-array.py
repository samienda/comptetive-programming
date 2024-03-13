class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        left, right = 0, n - 1

        while left <= right:

            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                first = last = mid
                while first - 1 >= 0 and nums[first - 1] == target:
                    first -= 1

                while last + 1 <  n and nums[last + 1] == target:
                    last += 1

                return [first, last]

        return [-1, -1]
        