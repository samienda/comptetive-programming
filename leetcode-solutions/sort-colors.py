class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # lets use selection sort just as an example
        n = len(nums)

        for i in range( n- 1):
            idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[idx]:
                    idx = j

            nums[i], nums[idx] = nums[idx], nums[i]

        return nums

                 
        