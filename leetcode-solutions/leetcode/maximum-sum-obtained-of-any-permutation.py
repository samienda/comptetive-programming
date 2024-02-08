class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # weight = [[] for i in range(len(requests) + 1)]
        n = len(nums)

        prefix = [0] * (n + 1)

        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1

        running = 0
        # print(prefix)
        for i in range(n):
            running += prefix[i]
            prefix[i] = running

        prefix.pop()

        prefix.sort()
        nums.sort()
        print(prefix)
        print(nums)
        
        _sum = 0
        for i in range(n):
            _sum += (prefix[i] * nums[i])

        return _sum % (10**9 + 7)



        





        