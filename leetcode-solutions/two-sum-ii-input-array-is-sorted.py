class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        left = 0
        right = len(n) - 1

        while left < right:
            curr = n[left] + n[right]
            if curr < target:
                left += 1
            elif curr > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        return []
        