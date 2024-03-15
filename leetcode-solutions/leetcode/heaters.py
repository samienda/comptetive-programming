class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def isvalid(rad):
            covered = [[h - rad, h + rad] for h in heaters]

            idx = 0
            for l, r in covered:

                while idx < len(houses) and l <= houses[idx] <= r:
                    
                    idx += 1

                if idx >= len(houses):
                    break

            if idx < len(houses):
                return False
            return True 

        
        low = 0
        high = 10**9

        while low < high:
            mid = (low + high) // 2

            if isvalid(mid):
                high = mid
            else:
                low = mid + 1

        return high