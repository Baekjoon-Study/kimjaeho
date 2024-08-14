import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    cond = list(map(int, sys.stdin.readline().split()))
    tmp = []
    tmp.extend(cond)
    tmp.extend(cards)
    cnt_cond = {k:0 for k in tmp}

    for i in cards:
        cnt_cond[i] += 1

    for i in cond:
        print(cnt_cond[i], end=' ')