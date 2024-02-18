class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda item:item[1], reverse=True)


        total = 0

        for num, unit in boxTypes:
            x = num
            if x > truckSize:
                x = truckSize
            total += (x * unit)
            truckSize -= x

            if not truckSize:
                break

        return total


        