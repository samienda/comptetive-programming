class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)

        freq = defaultdict(int)

        count = 0
        for ch in s:
            freq[ch] += 1
            
            if ch == '1':
                freq['01'] += freq['0']
                count += freq['10']
            else:
                freq['10'] += freq['1']
                count += freq['01']

        return count

        