# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(-1)
        for i in range(n + 1):

            while 0 <= nums[i] <= n and nums[i] != i and  nums[i] != nums[nums[i]]:
                idx = nums[i]
                nums[i], nums[idx] = nums[idx], nums[i]

        # print(n)

        for i in range(1, n + 1):
            if i != nums[i]:return i
        return n + 1