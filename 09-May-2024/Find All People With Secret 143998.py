# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set()
        secrets.add(0)
        secrets.add(firstPerson)

        time_based = {}
        for src, dest, t in meetings:
            if t not in time_based:
                time_based[t] = defaultdict(list)

            time_based[t][src].append(dest)
            time_based[t][dest].append(src)

        def dfs(node, graph):
            if node in visted:return

            visted.add(node)
            secrets.add(node)
            for nbs in graph[node]:
                dfs(nbs, graph)


        for t in sorted(time_based):
            visted = set()
            for src in time_based[t]:
                if src in secrets:
                    dfs(src, time_based[t])
        
        return secrets
