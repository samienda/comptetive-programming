class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        stack = []
        before = nums[:]


        for i in range(n):

            while stack and nums[stack[-1]] < nums[i]:
                nums[stack.pop()] = nums[i]

            stack.append(i)

        # print(stack)
        for i in range(n):

            while stack and nums[stack[-1]] < before[i]:
                # print(i, stack)
                nums[stack.pop()] = before[i]


        while stack:
            nums[stack.pop()] = -1
            
        return nums


        