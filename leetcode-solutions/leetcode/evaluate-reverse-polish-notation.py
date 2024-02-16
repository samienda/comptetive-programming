class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        add = '+'
        sub = '-'
        multiply = '*'
        divide = '/'

        for token in tokens:
            if token in '+-*/':
                a = stack.pop()
                b = stack.pop()

                # operations 
                if token == add:
                    stack.append(a + b)
                elif token == sub:
                    stack.append(b - a)
                elif token == multiply:
                    stack.append(a * b)
                else:
                    ans = b / a
                    if ans > 0:
                        stack.append(math.floor(ans))
                    else:
                        stack.append(math.ceil(ans))
            else:
                stack.append(int(token))
            
            # print(stack)

        return stack[0]