class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            nums[i] **= 2

        return sorted(nums)

        