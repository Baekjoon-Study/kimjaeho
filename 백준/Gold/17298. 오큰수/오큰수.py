import sys

n = int(sys.stdin.readline())

nge = list(map(int, sys.stdin.readline().split()))
result = [-1] * n

# for i in range(n):
#     idx = i+1
#     while idx < len(nge):
#         if nge[i] < nge[idx]:
#             result[i] = nge[idx]
#             break
#         idx += 1
    

stack = []

for i in range(n):
    while stack and nge[stack[-1]] < nge[i]:
        result[stack.pop()] = nge[i]
    stack.append(i)

print(' '.join(map(str, result)))
