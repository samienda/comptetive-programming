class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)


        first = 0
        second = 0
        
        while first < n and second < m:
            if nums1[first] == nums2[second]:
                return nums1[first]
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                first += 1


        return -1