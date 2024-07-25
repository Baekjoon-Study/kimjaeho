import sys

number = [1] * 1000001
number[0], number[1] = 0, 0

for i in range(2, int(len(number) ** 0.5) + 1):
    if number[i]:
        for j in range(i * i, 1000001, i):
            number[j] = 0

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    found = False
    for i in range(3, n // 2 + 1, 2): # n의 양끝에서 탐색을 시작하여 더해보는 것.
        # 이때 짝수는 소수일 수가 없기 때문에 3부터 2씩 건너뛰어 홀수만 탐색한다.
        if number[i] and number[n - i]: # 둘 다 소수이면
            print(f"{n} = {i} + {n - i}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")

