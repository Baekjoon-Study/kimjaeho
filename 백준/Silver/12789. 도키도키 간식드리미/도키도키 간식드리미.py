import sys

n = input()
line = list(map(int, input().split()))
stack = []
target = 1
for i in line:
    stack.append(i)
    while stack and stack[-1] == target: # target 추가했으면 pop
        stack.pop()
        target += 1
    if len(stack) > 1 and stack[-1] > stack[-2]: # stack이 존재, 순서대로 출력 가능하면
        print("Sad")
        sys.exit()
if stack:
    print("Sad")
else:
    print("Nice")