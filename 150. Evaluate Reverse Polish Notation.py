class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arith = ['+','*','/','-']

        def calc(x1,x2,op):
            if op == '+':
                return x1 + x2
            elif op == '/':
                return int(x1 / x2)
            elif op == '*':
                return x1 * x2
            elif op == '-':
                return x1 - x2

        for x in tokens:
            if x not in arith:
                stack.append(int(x))
            else:
                x2 = stack.pop()
                x1 = stack.pop()
                res = calc(x1,x2,x)
                stack.append(int(res))
                
        return stack[0]
      
