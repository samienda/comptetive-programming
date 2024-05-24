# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for w in word:
            index = ord(w) - ord('a')
            if not curr.children[index]:
                newnode = TrieNode()
                curr.children[index] = newnode

            curr = curr.children[index]

        curr.isEnd = True

    def dfs(self, node, word):
        queue = deque()
        for idx in range(25, -1, -1):
            nbs = node.children[idx]
            if nbs:
                queue.append((nbs, word + [chr(ord('a') + idx)]))

        answer = []
        if node.isEnd:
            answer.append("".join(word))
        while queue:
            node, path = queue.pop()
            # print(queue)
            if node.isEnd:
                answer.append("".join(path))

            if len(answer) > 2:break

            for idx in range(25, -1, -1):
                nbs = node.children[idx]
                
                if nbs:
                    queue.append((nbs, path + [chr(ord('a') + idx)]))

        return answer


    
    def suggest(self, word):
        allSuggestions = [[] for _ in range(len(word))]
        prefix = []

        root = self.root
        for i, w in enumerate(word):
            prefix.append(w)
            index = ord(w) - ord('a')
            if not root.children[index]:
                break

            root = root.children[index]
            currSuggestion = self.dfs(root, prefix)
            if not currSuggestion:break
            allSuggestions[i] = currSuggestion


        
        return allSuggestions

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()
        for word in products:
            trie.insert(word)


        
        return trie.suggest(searchWord)
        

