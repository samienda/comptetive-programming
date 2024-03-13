class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort(reverse=True)

        running = sum(nums)

        for num in nums:
            running -= num
            if running > num:
                return running + num

        
        return -1