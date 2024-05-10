# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def pick(idx, curr):
            if idx >= len(nums):
                if curr == target:return 1
                return 0

            state = (idx, curr)
            if state not in memo:
                memo[state] = pick(idx + 1, curr + nums[idx]) + pick(idx + 1, curr - nums[idx])
            return memo[state]
        return pick(0, 0)