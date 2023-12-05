class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        games = 0
        while n > 1:
            teams = n // 2
            games += teams

            if n % 2 != 0:
                teams += 1
            
            n = teams


        return games
            
                