class Solution:
    def minMoves(self, target: int, d: int) -> int:
        
        move = 0
        while target > 1:
            if d > 0:
                if target % 2 == 0:
                    target //= 2
                    d -= 1
                else:
                    target -= 1

                move += 1
            else:
                move += target - 1
                target = 1

        return move
        