class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        check = set(nums)

        if len(check) < 3:
            return False
        



        for i in range(n - 2):
            left = i + 1
            
            while left < n - 1:
                right = n - 1
                while nums[i] >= nums[left]  and left + 1 < right:
                    left += 1


                while nums[left] >= nums[right] and left < right - 1:
                    right -= 1


                print(nums[i], nums[left], nums[right])
                if nums[i] < nums[left] < nums[right]:
                    return True

                left += 1

            
        return False 




        