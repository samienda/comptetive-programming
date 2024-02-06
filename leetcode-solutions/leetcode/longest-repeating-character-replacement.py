class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)


        left = [0] * 26
        k = [k] * 26


        s = s.lower()
        print(s)

        for right in range(n):

            for i in range(26):
                # print(chr(i + ord('a')))
                if s[right] != chr(i + ord('a')):
                    k[i] -= 1

            # print(k)

            for j in range(26):
                if k[j] < 0:
                    if s[left[j]] != chr(j + ord('a')):
                        k[j] += 1

                    left[j]  += 1

        
        # print(left)

        ans = n - min(left)

        return ans