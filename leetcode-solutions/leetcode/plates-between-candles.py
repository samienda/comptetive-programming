class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        running = 0
        candles = []
        prefix = defaultdict(int)


        for i in range(n):
            if s[i] == '*':
                running += 1
            else:
                candles.append(i)
                prefix[i] = running

        # print(prefix)
        # print(candles)

        ans = []
        for left, right in queries:
            low = bisect.bisect_left(candles, left)
            high = bisect.bisect_right(candles, right)

            if low == high:
                ans.append(0)
            else:
                ans.append(prefix[candles[high - 1]] - prefix[candles[low]])

        return ans


        return [0]


