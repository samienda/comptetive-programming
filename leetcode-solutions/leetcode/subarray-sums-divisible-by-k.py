class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # nums.insert(0, 0)
        freq = Counter([0])

        count = 0
        running = 0
        for i in range(n):
            running += nums[i]
            nums[i] = running / k
            remainder = round(nums[i] % 1, 5)

            if remainder in freq:
                count += freq[remainder]

            freq[remainder] += 1

        
        print(nums)
        # for r in range(1, n + 1):
        #     for l in range(r):
        #         curr = nums[r] - nums[l]
        #         if curr % 1 == 0:
        #             count += 1


        return count
        