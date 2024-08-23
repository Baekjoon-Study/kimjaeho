import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    p = sorted(list(map(int, sys.stdin.readline().split())))

    result = 0
    accumulate = 0
    for i in p:
        accumulate += i
        result += accumulate
    print(result)