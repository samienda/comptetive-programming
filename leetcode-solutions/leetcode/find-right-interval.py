class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n

        for i in range(n):
            intervals[i].append(i)

        intervals.sort()
        # print(intervals)

        def find(target):

            low = 0
            high = n - 1
            while low < high:
                mid = (low + high) // 2

                if target <= intervals[mid][0]:
                    high = mid
                else:
                    low = mid + 1

            return low

        for interval in intervals:
            j = find(interval[1])

            if intervals[j][0] >= interval[1]:
                ans[interval[-1]] = intervals[j][-1]

        return ans 




        return [0]