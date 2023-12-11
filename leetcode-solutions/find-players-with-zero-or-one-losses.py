class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser = {}
        result = [[],[]]

        for win, loss in matches:
            loser[loss] = 1 + loser.get(loss, 0)
            loser[win] = 0 + loser.get(win, 0)


        loser = sorted(loser.items(), key=lambda item:item[1])


        for player, lost in loser:
            if lost == 0:
                result[0].append(player)
            elif lost == 1:
                result[1].append(player)
           

        result[0].sort()
        result[1].sort()
        return result
        