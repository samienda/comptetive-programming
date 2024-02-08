class Solution:
    def bestClosingTime(self, cust: str) -> int:
        n = len(cust)
        weight = []


        count = defaultdict(list)

        # let go left check if there is n in leftside of the index
        have = Counter()
        for i in range(n + 1):
            # print(have['N'])
            count[i].append(have['N'])

            if i < n and cust[i] == 'N':
                have[cust[i]] += 1


        for i in range(n, -1, -1):
            if i < n and cust[i] == 'Y':
                have[cust[i]] += 1

            # print(have['Y'])
            count[i].append(have['Y'])



        
        for j in range(n + 1):
            penality = sum(count[j])
            
            weight.append([penality, j])
        weight.sort()

        return weight[0][1]


            


        