class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)

        memo = deque()
        ans = [0] * n

        for i in range(n - 1, -1, -1):

            idx = bisect.bisect_left(memo, nums[i])
            ans[i] = idx
            memo.insert(idx, nums[i])

        return ans






        