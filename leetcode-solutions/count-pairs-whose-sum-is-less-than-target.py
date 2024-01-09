class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)

        count = 0
        for i in range(n):
            value = target - nums[i]
            for j in range(i + 1, n):
                if nums[j] < value:
                    count += 1


        return count 
        