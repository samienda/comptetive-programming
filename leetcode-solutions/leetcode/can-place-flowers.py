class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        fb = [0] + flowerbed
        fb.append(0)
        for i in range(1, m + 1):

            if fb[i - 1] == fb[i] == fb[i + 1] == 0:
                n -= 1
                fb[i] = 1

        return n < 1
        