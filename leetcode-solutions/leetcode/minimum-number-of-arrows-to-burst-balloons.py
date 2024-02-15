class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item:item[1])

        lastshot = float('-inf')
        shots = 0

        for start, end in points:
            if start > lastshot:
                lastshot = end
                shots += 1


        # print(points)
        return shots

        