class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        sums = sum(nums[:k])
        ave = sums / k


        for i in range(k, n):
            sums += nums[i] - nums[i - k]
            ave = max(ave, sums/k)

        return ave
