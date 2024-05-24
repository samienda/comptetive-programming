# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

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
                curr.children[index] = TrieNode()

            curr = curr.children[index]

        curr.isEnd = True

    def count(self, word, checker):
        curr = self.root
        ans = []
        for i, w in enumerate(word):
            index = ord(w) - ord('a')
            if not curr.children[index] or curr.isEnd or w != checker[i]:
                return "".join(ans)

            ans.append(w)
            curr = curr.children[index]

        return "".join(ans)

    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1: return strs[0]

        trie = Trie()
        for word in strs:
            trie.insert(word)

        ans = []
        for word in strs[1:]:
            prefix = trie.count(word, strs[0])
            ans.append((len(prefix), prefix))
        
        # print(ans)
        return sorted(ans)[0][-1]
