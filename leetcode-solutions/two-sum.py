class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)


        for i in range(n-1):
            value = target - nums[i]
            
            if value in nums[i + 1:]:
                first = i
                second = nums[i+1:].index(value) + i + 1
                return [first, second]


        

