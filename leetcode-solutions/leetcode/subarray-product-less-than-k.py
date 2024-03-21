class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        running = 1
        count = 0
        for right in range(n):
            running *= nums[right]

            while left <= right and running >= k:
                running /= nums[left]
                left += 1

            count += right - left + 1
        
        return count
        