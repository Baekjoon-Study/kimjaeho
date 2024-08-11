import sys

n = int(sys.stdin.readline())

spots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
spots.sort(key=lambda x:(x[1], x[0]))

for i in spots:
    print(' '.join(map(str, i)))