class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        freq = Counter([0])


        running = 0
        count = 0
        for i in range(n):
            running += nums[i]
            nums[i] = running

            if running - goal in freq:
                count += freq[running - goal]

            freq[running] += 1


        # nums = [0] + nums

        # count = 0
        # for r in range(1, n + 1):
        #     for l in range(r):
        #         if nums[r] - nums[l] == goal:
        #             count += 1 


        return count

