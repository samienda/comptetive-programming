class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        for i in range(n - 1):
            flag = False

            j = 0
            c = len(words[i])
            a = len(words[i + 1])
            m = min(c, a)
            while j < m:
                curr = order.index(words[i][j])
                after = order.index(words[i + 1][j])
                # print(curr, order[curr], after, order[after])
                
                if curr < after:
                    # print("break")
                    break
                elif curr > after :
                    return False
                
                j += 1
            else:
                if a < c:
                    return False 


        return True
