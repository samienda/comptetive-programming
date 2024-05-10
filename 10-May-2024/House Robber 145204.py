# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def pick(idx):

            if idx in memo:
                return memo[idx]

            if idx >= len(nums):
                return 0

            memo[idx] = max(pick(idx + 2), pick(idx + 3)) + nums[idx]

            return memo[idx]

        return max(pick(0), pick(1))

