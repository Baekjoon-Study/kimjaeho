import sys
li = [0] * 26
word = sys.stdin.readline().strip()
for i in word:
    li[ord(i) - 97] += 1

print(' '.join(map(str, li)))