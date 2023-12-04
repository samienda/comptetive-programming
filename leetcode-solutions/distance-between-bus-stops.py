class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)

        x = start
        y = destination
        if start > destination:
            x = destination
            y = start

        road = []
        

        dir1 = 0
        dir2 = 0

        for i in range(x, y):
            dir1 += distance[i]
            road.append(i)

        for i in range(n):
            if i not in road:
                dir2 += distance[i]


        return min(dir1, dir2)


        