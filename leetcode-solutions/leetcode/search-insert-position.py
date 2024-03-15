class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n

        while low < high:

            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid

        return high