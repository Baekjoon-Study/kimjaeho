import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    site = {}
    for _ in range(n):
        tmp1 = sys.stdin.readline().split()
        site[tmp1[0]] = tmp1[1]

    for _ in range(m):
        tmp2 = sys.stdin.readline().rstrip()
        print(site[tmp2])