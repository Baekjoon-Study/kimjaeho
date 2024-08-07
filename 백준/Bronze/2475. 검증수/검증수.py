import sys

if __name__ == '__main__':
    li = list(map(int, sys.stdin.readline().split()))
    rst = 0
    for i in li:
        rst += i**2
    print(rst % 10)