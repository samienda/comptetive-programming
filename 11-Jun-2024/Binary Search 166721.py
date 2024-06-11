# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # def divide(left, right):
        left, right  = 0, len(nums) - 1
        while left <= right:
            
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid

        return -1
        #     return divide(left, right)

        # return divide(0, len(nums) - 1)
        