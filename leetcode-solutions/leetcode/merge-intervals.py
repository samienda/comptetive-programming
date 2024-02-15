class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda item:item[1])


        laststart, lastend = intervals[0][0], intervals[0][1]
        res = []
        for start, end in intervals:
            if start > lastend:
                res.append([laststart, lastend])
                laststart = start
                lastend = end
            else:
                lastend = end
                if laststart > start:
                    laststart = start

        res.append([laststart, lastend])
        res.sort()
        ans = []

        laststart, lastend = res[0][0], res[0][1]
        for start, end in res:
            if start > lastend:
                ans.append([laststart, lastend])
                laststart = start
                lastend = end
            else:
                if lastend < end:
                    lastend = end

        ans.append([laststart, lastend])
        return ans



        