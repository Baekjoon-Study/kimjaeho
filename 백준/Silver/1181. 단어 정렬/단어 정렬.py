import sys

n = int(input())
s = [sys.stdin.readline().rstrip() for _ in range(n)]

s = list(set(s))
s.sort()
s.sort(key=len)

for i in s:
    print(i)