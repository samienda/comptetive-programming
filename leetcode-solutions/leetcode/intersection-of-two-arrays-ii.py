class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first = Counter(nums1)
        res = []

        for num in nums2:
            if first[num] > 0:
                res.append(num)
                first[num] -= 1

        return res