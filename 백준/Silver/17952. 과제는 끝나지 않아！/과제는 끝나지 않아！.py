import sys

if __name__ == '__main__':

    n = int(input())
    total = 0

    time = []
    score = []

    is_working = 0

    now_time = 0
    now_score = 0


# 과제 중인데 새 과제가 들어옴
# 과제 중인데 시간만 지나감
# 과제 끝났는데 새 과제가 들어옴
# 과제 끝났는데 시간만 지나감

# 과제를 다했음ㅇ

    for _ in range(n):
        assign = list(map(int, sys.stdin.readline().split()))
        if is_working:
            if assign[0] == 1:
                time.append(now_time)
                score.append(now_score)

                now_time = assign[2] - 1
                now_score = assign[1]
            else:
                now_time -= 1

            if now_time == 0:
                total += now_score
                if time:
                    now_time = time.pop()
                    now_score = score.pop()
                else:
                    is_working = 0
        else:
            if assign[0] == 1:
                is_working = 1
                now_time = assign[2] - 1
                now_score = assign[1]
            else:
                continue

    print(total)
        