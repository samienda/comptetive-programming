class Solution:
    def balancedStringSplit(self, s: str) -> int:

        count = Counter()
        ans = 0
        for ch in s:
            count[ch] += 1

            if count['R'] == count['L']:
                ans += 1

        return ans
        