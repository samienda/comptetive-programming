class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)


        right = n - 1
        left = 0

        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left] = nums[right]
                left += 1
                right -= 1
            else:
                left += 1


        return right + 1




        