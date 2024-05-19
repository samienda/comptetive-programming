# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for x in range(target + 1):
            for num in nums:
                idx = x + num
                if idx <= target:
                    dp[idx] += dp[x]

        return dp[-1]