class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        mod = 10 ** 9 + 7

        nums.sort()

        count = 0
        for left in range(n):

            value = target - nums[left]

            right = bisect.bisect_right(nums, value)
            if right > left:
                count += 2 ** (right - left - 1)

        return count % mod


