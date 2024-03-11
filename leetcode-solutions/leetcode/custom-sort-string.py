class Solution:
    def customSortString(self, order: str, s: str) -> str:
        string = list(s)
        def compare(item):
            return order.index(item) if item in order else -1

        # print(string)
        string.sort(key=compare)

        return "".join(string)
        