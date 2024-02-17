class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        total = 0
        for i in range(n):
            if i % 2 == 0:
                total += nums[i]

        return total

        