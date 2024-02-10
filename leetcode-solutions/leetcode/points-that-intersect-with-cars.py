class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * 102


        for start, end in nums:
            prefix[start] += 1
            prefix[end + 1] -= 1

        count = 0
        for i in range(1, 102):
            prefix[i] += prefix[i - 1]

            if prefix[i] > 0:
                count += 1

        return count

        