class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split('/')
        for ch in path:
            if ch ==  '..':
                if stack:
                    stack.pop()
            elif ch in '//.':
                continue
            else:
                stack.append(ch)

        return '/' +  "/".join(stack)

        # res = ''
        # for path in stack:
        #     res += '/' + path


        # return res if res else '/'
        