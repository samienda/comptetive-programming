class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        _max = float('-inf')
        running = 0
        for i in range(n):
            running += nums[i]
            
            _max = max(_max, running)

            if running < 0:
                running = 0

        return _max
        