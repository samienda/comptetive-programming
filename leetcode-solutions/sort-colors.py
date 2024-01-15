class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        left = 0
        right = 0

        while right < n:

            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1

            right += 1

        right = left

        while right < n:

            if nums[right] == 1:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1

            right += 1

        right = left

        while right < n:

            if nums[right] == 2:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1

            right += 1

        
