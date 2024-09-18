import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    c = a-b
    # print(c)
    d = b-a
    # print(d)
    result = c.union(d)
    # print(result)
    print(len(result))
    