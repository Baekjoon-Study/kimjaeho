# 3009
import sys

x = {}
y = {}
for _ in range(3):
    xx, yy = map(int, sys.stdin.readline().split())
    try:
        x[xx] += 1
    except:
        x[xx] = 1
    try:
        y[yy] += 1
    except:
        y[yy] = 1
print(min(x, key=x.get), min(y, key=y.get))