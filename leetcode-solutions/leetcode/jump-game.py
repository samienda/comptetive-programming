class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = nums[-1]

        n = len(nums)

        for i in range(n - 1, -1, -1):
            if nums[i] + i >= good:
                good = i

        return good == 0
        