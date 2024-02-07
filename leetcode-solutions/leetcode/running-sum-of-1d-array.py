class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        curr = 0
        for i in range(n):
            curr += nums[i]

            nums[i] = curr


        return nums