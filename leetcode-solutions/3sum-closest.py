class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        close = 0
        close_diff = float('inf')


        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                value = nums[i] + nums[left] + nums[right]
                if abs(value  - target) < close_diff:
                    close = value
                    close_diff = abs(value - target)

                if value > target:
                    right -= 1
                elif value < target:
                    left += 1
                else:
                    break
        
        return close
        