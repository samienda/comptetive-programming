class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        seeker = 0
        ph = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                seeker += 1
            else:
                nums[seeker], nums[ph] = nums[ph], nums[seeker]
                seeker += 1
                ph += 1
                
                 


