import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    never_heard = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
    never_seen = sorted([sys.stdin.readline().rstrip() for _ in range(m)])

    never = []

    i = 0
    j = 0
    while (i < n) & (j < m):
        if never_heard[i] == never_seen[j]:
            never.append(never_seen[j])
            i += 1
            j += 1
        elif never_heard[i] < never_seen[j]:
            i += 1
        elif never_heard[i] > never_seen[j]:
            j += 1

    print(len(never))
    for i in never:
        print(i)