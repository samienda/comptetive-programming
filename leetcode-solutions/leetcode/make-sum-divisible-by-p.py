class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        freq = {0: -1}
        k = sum(nums) % p

        count = float('inf')

        if k == 0:
            return 0

        running = 0
        for i in range(n):
            running += nums[i]
            nums[i] = running

            if (running - k) % p in freq:
                count = min(count, i - freq[(running - k) % p])



            freq[running % p] =  i
        

        return count if (count != float('inf') and count != len(nums)) else -1



        