class Solution:
    def minOperations(self, nums: List[int]) -> int:

        oper = 0

        last = nums[0]

        for num in nums[1:]:
            if num <= last:
                oper += (last -  num + 1)
                last += 1
            else:
                last = num
        
        return oper

        