class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)

        count = 0
        window = sum(arr[:k - 1])

        for right in range(k - 1, n):
            window += arr[right]

            ave = window / k

            if ave >= threshold:
                count += 1

            window -= arr[right - k + 1] 

        return count

        