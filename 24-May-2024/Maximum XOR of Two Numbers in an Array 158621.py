# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None, None]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            curr = int(ch)
            if not node.children[curr]:
                newnode = TrieNode()
                node.children[curr] = newnode
            node = node.children[curr]
            
        node.is_end = True

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        def change(num):
            bit = ['0' for _ in range(32)]

            for i, b in enumerate(reversed(bin(num)[2:])):
                bit[i] = b

            return bit[::-1]

        trie = Trie()
        for num in nums:
            # print(num, change(num))
            trie.insert(change(num))


        def find(num):
            # print(num)
            bits = trie.root
            ans = []
            for b in num:
                # print(b, bits.children)
                if b == '1' and bits.children[0]:
                    bits = bits.children[0]
                    ans.append(b)
                elif b == '0' and bits.children[1]:
                    bits = bits.children[1]
                    ans.append('1')
                else:
                    bits = bits.children[int(b)]
                    ans.append('0')
                # print(ans)

            return int("".join(ans), 2)


        
        maximum = 0
        for num in nums:
            maximum = max(
                maximum,
                find(change(num))
            )
        

        return maximum

        