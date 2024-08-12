import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

rst = str(a * b * c)
dict = {str(k):0 for k in range(10)}
for i in rst:
    dict[i] += 1

for i in dict.values():
    print(i)