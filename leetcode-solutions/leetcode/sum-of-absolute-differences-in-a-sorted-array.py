class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)


        prefix = [0]

        running = 0
        for i in range(n):
            running += nums[i]
            prefix.append(running)

        # print(prefix)

        for i in range(n):
            ans = ((i + 1) * nums[i]) - (prefix[i])
            ans += (prefix[n] - prefix[i + 1]) - ((n - i) * nums[i])

            nums[i] = ans


        return nums