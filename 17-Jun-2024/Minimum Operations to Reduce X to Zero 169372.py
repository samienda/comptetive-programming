# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        l = 0

        windowsum = 0
        oper = -1

        value = sum(nums) - x


        for r in range(n):
            windowsum += nums[r]

            while windowsum > value and l <= r:
                windowsum -= nums[l]
                l += 1

            if windowsum == value:
                oper = max(oper, r - l + 1)


        return -1 if oper == -1 else n - oper


        