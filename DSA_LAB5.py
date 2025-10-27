def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/' or op == '%':
        return 2
    if op == '^':
        return 3
    return 0

def isOperand(ch):
    return ch.isalnum()

def infix_to_postfix(expression):
    stack = []  # stack for operators
    output = []  # list for output (postfix)

    for char in expression:
        if isOperand(char):
            output.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '('

        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

if __name__ == "__main__":
    expr = input("Enter an infix expression: ")
    postfix = infix_to_postfix(expr.replace(" ", ""))  # remove spaces
    print("Postfix Expression:", postfix)
