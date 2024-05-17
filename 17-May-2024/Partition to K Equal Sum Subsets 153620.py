# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        target = sum(nums)/k
        n = len(nums)

        if sum(nums) % k != 0:return False

        if n == k:
            return target == nums[-1]

        @cache
        def dp(mask, curr):
            if mask == (1 << n) - 1:
                return curr == target

            if curr == target:
                return dp(mask, 0)

            # state = (mask, curr)
            # if state not in memo:
            for i, num in enumerate(nums):
                if (mask & 1 << i) != 0:
                    continue

                if dp(mask | 1 << i, curr + num):
                    return True

        return dp(0, 0) 