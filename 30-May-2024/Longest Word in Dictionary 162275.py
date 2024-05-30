# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not root.children[index]:
                newnode = TrieNode()
                root.children[index] = newnode

            root = root.children[index]

        root.isEnd = True

    def check(self, word):
        root = self.root
        count = 0
        for i, w in enumerate(word):
            index = ord(w) - ord('a')
            if not root or not root.children[index]:
                count += 1

            if count > 1:
                return False

            if root:
                root = root.children[index]

        return True

    def longest(self):
        root = self.root
        queue = deque()

        queue.append((root, []))
        maximum = []
        while queue:
            node, path = queue.popleft()
            if len(path) > len(maximum):
                maximum = path


            for i in range(26):
                if node.children[i]:
                    queue.append((node.children[i], path + [chr(i + ord('a'))]))

        return maximum

            

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda item:len(item))
        # print(words)

        trie = Trie()
        for word in words:

            if trie.check(word):
                trie.insert(word)

        return "".join(trie.longest())
        