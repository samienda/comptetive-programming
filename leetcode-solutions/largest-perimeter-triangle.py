class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        # sort so that we make sure that start from largest values
        nums.sort(reverse=True)

        i = 0
        while i < n - 2:
            # so each time we are going to take highest values of untries lengths
            
            #  we name the three sides 
            c, b, a = nums[i], nums[i + 1], nums[i + 2]
          


            if a + b > c:
                return a + b + c

            i += 1

        return 0


