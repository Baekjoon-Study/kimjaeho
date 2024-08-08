import sys
n = int(input())
mem_list = [(sys.stdin.readline().split()) for _ in range(n)]
mem_list = sorted(mem_list, key=lambda x: int(x[0]))
for i in mem_list:
    print(' '.join(i))