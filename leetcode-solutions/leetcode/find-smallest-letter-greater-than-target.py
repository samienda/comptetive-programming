class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)

        low = 0
        high = n

        while low < high:
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1

        # print(low, high)
        return letters[high] if high < n else letters[0]
        