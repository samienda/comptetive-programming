class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter([0])
        # nums.insert(0, 0)

        count = 0
        curr = 0
        for i in range(n):
            curr += nums[i]
            nums[i] = curr

            if curr - k in freq:
                count+= freq[curr - k]

            freq[curr] += 1

        # print(nums)
        # print(freq)

        # for x in range(1, n + 1):
        #     for j in range(x):
        #         if nums[x] - nums[j] == k:
        #             count += 1

        return count
