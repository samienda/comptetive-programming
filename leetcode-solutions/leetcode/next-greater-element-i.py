class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        temp = defaultdict(int)

        for num in nums2:
            while stack and stack[-1] < num:
                temp[stack.pop()] = num

            stack.append(num)

        for i in range(len(nums1)):
            if nums1[i] in temp:
                nums1[i] = temp[nums1[i]]
            else:
                nums1[i] = -1

        return nums1