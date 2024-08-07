import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
C = int(sys.stdin.readline())

rst1 = int(A) + int(B) - C
rst2 = int(A + B) - C
print(rst1)
print(rst2)