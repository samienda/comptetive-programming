class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        prefix = nums[:]


        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        prefix.append(0)

        # print(nums)
        # print(prefix)
        # # return -1

        
        for large in range(n - 1, 1, -1):
            
            if nums[large] < prefix[large - 1]:
                return prefix[large]

        return -1
