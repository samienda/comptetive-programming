class Solution:
    def largestGoodInteger(self, num: str) -> str:
        yescase = [ "999", "888", "777", "666", "555","444","333" , "222", "111","000",]

        for yes in yescase:
            if yes in num:
                return yes


        return ""
        