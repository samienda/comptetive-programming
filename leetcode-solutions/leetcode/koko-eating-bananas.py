class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def isvalid(k):

            hours = 0
            for pile in piles:

                curr = math.ceil(pile/k)

                hours += curr

            return hours <= h

        
        low = 1
        high = 10**9

        while low < high:
            mid = (low + high) // 2

            if isvalid(mid):
                high = mid
            else:
                low = mid + 1

        return high
        