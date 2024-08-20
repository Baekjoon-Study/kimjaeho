import sys

def my_round(n):
    if n >= 0:
        return int(n + 0.5)
    else: return int(n - 0.5)

if __name__ == '__main__':
    n = int(sys.stdin.readline()) # n은 홀수
    li = sorted([int(sys.stdin.readline()) for _ in range(n)])
    mean = my_round(sum(li) / len(li))
    median = li[len(li) // 2]
    range = li[-1] - li[0]

    mode = 0
    cnt = {}
    for i in li:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

    mode = [k for k, v in cnt.items() if v==max(cnt.values())]
    if len(mode) > 1:
        mode = [mode[1]]

    print(mean)
    print(median)
    print(mode[0])
    print(range)