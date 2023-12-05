class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # count the number of modifications if it pass 1 break and return false
        count = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                # her we should how to modify and which to modify
                #  
                
                if i + 1 < n and nums[i + 1] < nums[i - 1]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                if count == 1:
                    return False
                count += 1
        


        return nums == sorted(nums)  

        
        