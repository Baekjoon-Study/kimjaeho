import sys

n = int(input())
mem_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
mem_list = sorted(mem_list, key=lambda x: (x[0], x[1]))
for i in mem_list:
    print(' '.join(map(str, i)))