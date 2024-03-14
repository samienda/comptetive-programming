class Solution:
    def hIndex(self, citations: List[int]) -> int:


        def higher(left, right):
            mid = (left + right) // 2
            
            if left >= right:
                return min(n - mid, citations[mid])
            
            if n - mid > citations[mid]:
                left = mid + 1
            elif n - mid < citations[mid]:
                right = mid
            else:
                return min(n - mid, citations[mid])
            
            return higher(left, right) 


        n = len(citations)
        return higher(0, n - 1)

        