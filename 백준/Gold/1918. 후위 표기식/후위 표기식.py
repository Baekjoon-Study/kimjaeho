import sys

expression = sys.stdin.readline().strip()
stack = []
operators = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2}

for i in expression:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            print(stack.pop(-1), end='')
        stack.pop(-1)
    elif (i == '+') or (i == '-') or (i == '*') or (i == '/'):
        while stack and operators[i] <= operators[stack[-1]]:
            print(stack.pop(-1), end='')
        stack.append(i)
    else:
        print(i, end='')

while stack:
    print(stack.pop(-1), end='')
