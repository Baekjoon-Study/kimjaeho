import sys

num = sys.stdin.readline().rstrip()

while num != '0':
    msg = 'yes' if num == num[::-1] else 'no'
    print(msg)

    num = sys.stdin.readline().rstrip()