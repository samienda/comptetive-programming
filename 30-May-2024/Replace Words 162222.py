# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
                root.children[index] = TrieNode()

            root = root.children[index]
        root.isEnd = True

    
    def find(self, word):
        count = 0
        root = self.root

        for w in word:
            index = ord(w) - ord('a')
            if root.isEnd:
                return count

            if not root.children[index]: return -1

            root = root.children[index]
            count += 1

        return count
    

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        sentence = sentence.split(" ")

        answer = []
        for word in sentence:
            count = trie.find(word)
            answer.append(word[:count] if count > 0 else word)

        return " ".join(answer)