class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n = len(list1)

        common_strings = []

        for i in range(n):
            str1 = list1[i]


            if str1 in list2:
                list2_index = list2.index(str1)
                
                common_strings.append([i + list2_index, str1])



        common_strings.sort()

        minimum = common_strings[0][0]
        result = []

        for string in common_strings:
            if string[0] == minimum:
                result.append(string[1])


        return result









        