class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = []

        for i in range(n):
            moves = 0
            for j in range(n):
                if i != j and boxes[j] == "1":
                    moves += abs(j - i)

            res.append(moves)


        return res
