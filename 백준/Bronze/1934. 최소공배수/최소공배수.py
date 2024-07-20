import sys

def gcd(a, b):
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    gcd_value = gcd(a, b)
    print(a * b // gcd_value)
