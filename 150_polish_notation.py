def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == '+':
            stack[-2] += stack[-1]
            stack.pop()
        elif token == '-':
            stack[-2] -= stack[-1]
            stack.pop()
        elif token == '*':
            stack[-2] *= stack[-1]
            stack.pop()
        elif token == '/':
            stack[-2] //= stack[-1]
            stack.pop()
        else:
            stack.append(token)
    return stack[0]

