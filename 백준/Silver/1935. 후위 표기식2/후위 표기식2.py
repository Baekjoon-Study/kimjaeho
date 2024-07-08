import sys

n = int(sys.stdin.readline())
expression = sys.stdin.readline().strip()
stack = []
operand = []
operator = ['+', '-', '*', '/']
tmp = ''
for _ in range(n):
    operand.append(int(sys.stdin.readline()))

for i in expression:
    if i in operator:
        op2 = stack.pop(-1)
        op1 = stack.pop(-1)
        rst = 0
        if i == '+':
            rst = op1 + op2
        elif i == '-':
            rst = op1 - op2
        elif i == '*':
            rst = op1 * op2
        else:
            rst = op1 / op2
        stack.append(rst)
    else:
        stack.append(operand[ord(i) - 65])

print(f'{round(stack.pop(-1), 3):.2f}')