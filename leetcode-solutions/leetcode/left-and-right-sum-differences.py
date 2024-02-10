class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)


        for i in range(1, n):
            nums[i] += nums[i - 1]

        ans = [0] * n
        # print(nums)
        for i in range(1, n):
            ans[i]  = abs((nums[i - 1]) - (nums[n - 1] - nums[i]))

        ans[0] = abs(nums[n - 1] - nums[0])

        return ans 
        