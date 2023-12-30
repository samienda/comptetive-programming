class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort(reverse=True)
        count = 0
        res = 0
        for i in range(n - 1):
            count += 1
            if nums[i] == nums[i + 1]:
                continue
            else:
                res += count


        return res


