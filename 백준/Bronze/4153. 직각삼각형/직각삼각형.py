import sys

while True:
    triangle = sorted(map(int, sys.stdin.readline().split()))
    if triangle[2] == triangle[1] == triangle[0] == 0:
        break
    is_right = triangle[2]**2 == triangle[0]**2 + triangle[1]**2
    rst = "right" if is_right else "wrong"
    print(rst)
        
