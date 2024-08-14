import sys

parenthesis = {']':'[', ')':'('}

if __name__ == '__main__':
    while True:
        sentence = sys.stdin.readline().rstrip()
        if sentence == '.':
            break
        stack = []
        tmp = ''
        for i in sentence:
            if i == '[' or i == '(':
                stack.append(i)
            elif i == ']' or i == ')':
                if not len(stack):
                    print('no')
                    break
                if not parenthesis[i] == stack.pop(-1):
                    print('no')
                    break
            elif i == '.':
                if len(stack):
                    print('no')
                else:
                    print('yes')
                break
            else:
                pass
                