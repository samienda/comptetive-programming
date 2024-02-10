class Solution:
    def bestClosingTime(self, cust: str) -> int:
        curr_pen = min_pen = cust.count('Y')
        idx = 0
        n = len(cust)


        for i in range(n):
            if cust[i] == 'Y':
                curr_pen -= 1
            else:
                curr_pen += 1


            if curr_pen < min_pen:
                min_pen = curr_pen
                idx = i + 1


        return idx

        