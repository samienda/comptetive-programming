class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = []


        for start, end in ranges:
            covered = covered + [i for i in range(start, end + 1)]


        for i in range(left, right + 1):
            if i not in covered:
                return False
        


        return True