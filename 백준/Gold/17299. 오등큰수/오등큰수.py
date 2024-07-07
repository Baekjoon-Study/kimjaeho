import sys

n = int(sys.stdin.readline())

ngf = list(map(int, sys.stdin.readline().split()))
dict = {}
for i in ngf:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 0

result = [-1] * n

stack = []

for i in range(n):
    while stack and dict[ngf[stack[-1]]] < dict[ngf[i]]:
        result[stack.pop()] = ngf[i]
    stack.append(i)

print(' '.join(map(str, result)))