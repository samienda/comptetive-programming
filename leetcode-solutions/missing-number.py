class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        distinct_nums = list( range(n + 1))
        


        for num in distinct_nums:
            if num not in nums:
                return num
        

        re