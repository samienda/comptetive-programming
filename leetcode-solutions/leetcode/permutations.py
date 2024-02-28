class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        # called = []
        # check = set()
        def pick(curr, check):
            nonlocal res
            if len(curr) == len(nums):
                res.append(curr)
                return 

            for i in range(len(nums)): # O(n)
                # # called.append("called")
                if i not in check:
                    check.add(i)
                    pick(curr + [nums[i]], check)
                    check.remove(i)

        pick([], set())
        # print(len(called))
        return res
        