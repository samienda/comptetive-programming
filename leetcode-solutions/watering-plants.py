class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        def distance(start, destination):
            return start - destination



        capa = capacity
        n = len(plants)
        steps = 0


        for i in range(n):
            p = plants[i]
            if p > capa:
                capa = capacity
                steps += (2 * distance(i, -1)) - 1
            else:
                steps += 1

            capa -= p

            # print(steps)

        return steps
  