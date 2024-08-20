import sys

def power(a, b, m): # n 제곱을 재귀함수로 구현함.
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
            # print(f'result : {result}')
        b //= 2
        # print(f'b : {b}')
        a = (a * a) % m
        # print(f'a : {a}')
        # print()
    return result

if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())
    print(power(a,b,c))