class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)

        memo = deque()
        count = 0
        for i in range(n): # O(n)

            store = nums1[i] - nums2[i]
            check = nums1[i] - nums2[i] + diff

            count += bisect.bisect_right(memo, check) # O(logn)
            memo.insert(bisect.bisect_right(memo, store), store) # O(logn)

        return count