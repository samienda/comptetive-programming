class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        left = bisect.bisect_left(arr, x)
        right = bisect.bisect_right(arr, x) - 1
        

        while right - left + 1 < k:

                
            if 0 <= left - 1 <= right + 1 < n and abs(arr[right + 1] - x) < abs(arr[left - 1] - x):
                right += 1
            elif left - 1 < 0 <= right + 1 < n:
                right += 1
            else:
                left  -= 1


        return arr[left:right + 1] if k >= right - left + 1 else arr[left: left+ k]