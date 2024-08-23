import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    min_coin = 0

    value = []
    for _ in range(n):
        value.append(int(sys.stdin.readline()))
    
    i = -1
    while k != 0:
        min_coin += k // value[i]
        k %= value[i]
        i -= 1
    print(min_coin)