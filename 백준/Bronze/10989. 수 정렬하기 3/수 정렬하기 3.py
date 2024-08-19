import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    k = [0] * 10000
    for i in range(n):
        k[int(sys.stdin.readline())-1] += 1

    for i in range(len(k)):
        if k[i] != 0:
            for _ in range(k[i]):
                print(f'{i+1}')

