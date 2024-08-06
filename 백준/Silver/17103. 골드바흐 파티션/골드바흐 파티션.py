import sys

number = [1] * 1000001
number[0], number[1] = 0, 0

for i in range(2, int(len(number) ** 0.5) + 1):
    if number[i]:
        for j in range(i * i, 1000001, i):
            number[j] = 0

# ---------------------------------------------

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

# -----------------------------------------------

def my_result(n):
    # t = int(sys.stdin.readline().rstrip())
    # for i in range(t):
    # n = int(sys.stdin.readline().rstrip())
    cnt = 0

    if n == 4:
        return 1

    for i in range(3, n // 2 + 1, 2): # n의 양끝에서 탐색을 시작하여 더해보는 것.
        # 이때 짝수는 소수일 수가 없기 때문에 3부터 2씩 건너뛰어 홀수만 탐색한다.
        if number[i] and number[n - i]: # 둘 다 소수이면
            # print(f"{n} = {i} + {n - i}")
            cnt += 1

    return cnt


# ------------------------------------------------------


def result(N):

    # for _ in range(T):
    count = 0
    # N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    return count


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        n = int(sys.stdin.readline())
        print(result(n))
