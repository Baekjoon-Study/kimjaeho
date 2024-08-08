import sys

n = int(sys.stdin.readline())
for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    y = li[2] % li[0]
    x = (li[2] // li[0]) + 1
    if y == 0:
        y = li[0]
        x -=1
    print(y * 100 + x)