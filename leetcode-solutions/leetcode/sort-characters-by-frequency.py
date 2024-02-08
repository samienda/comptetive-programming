class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)
        count = Counter(s)

        def compare(item):
            return count[item]
        
        s = list(s)
        s.sort()
        s.sort(key=compare, reverse=True)

        print(s)
        return "".join(s)