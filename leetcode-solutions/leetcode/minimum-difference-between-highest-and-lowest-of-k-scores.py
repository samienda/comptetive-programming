class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()


        left = 0
        mini = nums[n - 1]

        for right in range(k - 1, n):
            mini = min(mini, nums[right] - nums[left])

            left += 1


        return mini


        