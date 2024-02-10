class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        # gain.insert(0, 0)

        height = max(0, gain[0])

        for i in range(1, n):
            gain[i] += gain[i - 1]

            height = max(height, gain[i])

        return height


        