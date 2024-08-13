import sys

n = int(sys.stdin.readline())
size = map(int, sys.stdin.readline().split())
t, p = map(int, sys.stdin.readline().split())

bundle = 0
for i in size:
    bundle += i // t + bool(i % t)

print(bundle)

bundle = n // p
print(bundle, end=' ')
print(n % p)