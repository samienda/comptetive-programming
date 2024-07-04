# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Union:
    def __init__(self, n):
        self.parent = [ i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, a):
        if a == self.parent[a]:return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


    def join(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)

        if self.rank[roota] > self.rank[rootb]:
            self.parent[rootb] = roota
        elif self.rank[rootb] > self.rank[roota]:
            self.parent[roota] = rootb
        else:
            self.parent[rootb] = roota
            self.rank[roota] += 1



class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        # edges.sort()
        union = Union(n)
        for a, b in edges:
            union.join(a, b)
        
        for i in range(n - 1, -1, -1):
            union.find(i)
        count = Counter(union.parent)
        # print(count)

        total = 0
        for i, v in count.items():
            n -= v
            total += (v * n)

        return total

        
