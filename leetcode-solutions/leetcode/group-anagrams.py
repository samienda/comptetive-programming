class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)


        dic = defaultdict(list)

        for word in strs:
            
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            dic[tuple(count)].append(word)


        return [value for key, value in dic.items()]