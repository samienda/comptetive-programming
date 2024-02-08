class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # nums.insert(0, 0)
        freq = [1] + [0] * k

        count = 0
        running = 0
        for num in nums:
            running = (num + running) % k
             
            count += freq[running]

            freq[running] += 1

        
        # for r in range(1, n + 1):
        #     for l in range(r):
        #         curr = nums[r] - nums[l]
        #         if curr % 1 == 0:
        #             count += 1


        return count