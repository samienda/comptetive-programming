class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)


        left = 0
        size = n + 1

        for right in range(n):
            target -= nums[right]

            while target <= 0:
                size = min(size, right - left + 1)

                target += nums[left]
                left += 1

        return size if size != n + 1 else 0


        