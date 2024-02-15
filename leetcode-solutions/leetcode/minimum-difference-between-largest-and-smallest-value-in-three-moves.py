class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mini = nums[0]
        maxi = nums[n - 1]

        if n > 3:
            first = nums[3] - maxi
            second = nums[n - 4] - mini
            third = nums[n - 3] - nums[1]
            fourth = nums[2] - nums[n - 2]

            return min(abs(first), abs(second), abs(third), abs(fourth))
        
        return 0
            