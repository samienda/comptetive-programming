class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return 
        
        for i in range(m, m + n):
            nums1[i], nums2[i - m] = nums2[i - m], nums1[i]

        for i in range(m + n):
            for j in range(1, n + m - i):
                if nums1[j] < nums1[j - 1]:
                    nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]

            
        