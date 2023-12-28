class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)


        hist = [0] * (max(heights) + 1)
        name = defaultdict(list)
        res = []


        for i in range(n):
            h = heights[i]
            hist[h] = names[i]


        for na in hist:
            if na != 0:
                res.append(na)


        return res[::-1]



        