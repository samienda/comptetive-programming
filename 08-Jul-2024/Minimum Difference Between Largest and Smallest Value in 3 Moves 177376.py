# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 5:
            return 0
        
        nums.sort()
        return min(
            nums[n - 1] - nums[3],
            nums[n - 2] - nums[2],
            nums[n - 3] - nums[1],
            nums[n - 4] - nums[0],
        )