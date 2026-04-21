class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # append if you see numbers
        # pop if you see operators
        # append the result back in

        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token.isdigit() or (token.startswith('-') and len(token) > 1):
                stack.append(int(token))
            
            elif token in operators:
                
                if len(stack) >= 2:
                
                    var_2 = stack.pop()
                    var_1 = stack.pop()
                    
                    if token == '*':
                        stack.append(var_1 * var_2)
                    elif token == '-':
                        stack.append(var_1 - var_2)
                    elif token == '+':
                        stack.append(var_1 + var_2)
                    elif token == '/':
                        stack.append(int(var_1 / var_2))
                        
        return stack[-1]