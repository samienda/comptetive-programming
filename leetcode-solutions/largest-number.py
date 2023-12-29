class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        maxi = 0

        for i in range(n):
            nums[i] =str(nums[i])


        for i in range(n):
            for j in range(n  - 1):
                num1 = nums[j] 
                num2 = nums[j + 1] 
                if num1 + num2 < num2 + num1:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        res = "".join(nums)

        return str(int(res))
        
