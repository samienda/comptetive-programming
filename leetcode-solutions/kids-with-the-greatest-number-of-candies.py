class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        res = []

        for candy in candies:
            if candy + extraCandies >= maxi:
                res.append(True)
            else:
                res.append(False)

        return res