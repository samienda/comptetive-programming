class Solution:
    def splitString(self, s: str) -> bool:
        # state idx, 
        final = False
        def split(last, left):
            nonlocal final

            if left >= len(s):
                if int(s) != last:
                    final = True
                # print(final)
                return 

            for idx in range(left + 1, len(s) + 1):
                # print("check", s[left:idx])
                if last == float('inf') or  int(s[left:idx]) + 1 == last:
                    # print( last, left)
                    split(int(s[left:idx]), idx)

        split(float('inf'), 0)
        return final
