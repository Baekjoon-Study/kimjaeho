import sys

word = sys.stdin.readline()[:-1]
result = []
for i in range(len(word)):
    result.append(word[i:])

for i in sorted(result):
    print(i)