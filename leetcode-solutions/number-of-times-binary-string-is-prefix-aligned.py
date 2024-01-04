class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)

        prefix = [i + 1 for i in range(n)]

        count = 0
        for i in range(1, n):
            flips[i] += flips[i-1]
            prefix[i] += prefix[i-1]

            if prefix[i] == flips[i]:
                count += 1

        return count if flips[0] != 1 else count + 1


