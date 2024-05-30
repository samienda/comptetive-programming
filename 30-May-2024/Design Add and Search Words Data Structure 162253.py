# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children =  [None for _ in range(26)]
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not root.children[index]:
                newnode = TrieNode()
                root.children[index] = newnode

            root = root.children[index]

        root.isEnd = True


    def search(self, word: str) -> bool:


        def dfs(idx, node):
            if idx >= len(word): return node.isEnd

            if word[idx] == '.':
                found = False
                for i in range(26):
                    if node.children[i]:
                        found = found or dfs(idx + 1, node.children[i])

                return found

            index = ord(word[idx]) - ord('a')

            return node.children[index] and dfs(idx + 1, node.children[index])


        return dfs(0, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)