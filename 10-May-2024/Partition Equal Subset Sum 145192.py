# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def pick(idx, target):
            if target <= 0 or idx >= len(nums):
                return target == 0


            state = (idx, target)
            if state not in memo:
                memo[state] = pick(idx + 1, target - nums[idx]) or pick(idx + 1, target)

            return memo[state]

        total = sum(nums)
        return total % 2 == 0 and pick(0, total // 2)