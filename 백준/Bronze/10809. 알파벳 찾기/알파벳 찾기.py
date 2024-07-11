import sys
li = [-1] * 26
word = sys.stdin.readline().strip()
for i in range(len(word)):
    if li[ord(word[i]) - 97] == -1:
        li[ord(word[i]) - 97] = i

print(' '.join(map(str, li)))