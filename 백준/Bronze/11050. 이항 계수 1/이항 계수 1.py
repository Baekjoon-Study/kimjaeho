import sys

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    print(int(factorial(n) / (factorial(n-k) * factorial(k))))