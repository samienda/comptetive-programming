class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        final = firstList + secondList
        # final.sort(key=lambda item:item[1])
        final.sort()

        last = final[0][1]
        res = []
        # stack = []

        for start, end in final[1:]:
            # if stack and stack[-1] > start:
            #     res.append([start, stack.pop()])
            if end < last:
                res.append([start, end])
                continue
            elif start <= last:
                res.append([start, last])
            elif end <= last:
                res.append(start, end)
            last = end
        # print(stack)


        # print(final)
        return res