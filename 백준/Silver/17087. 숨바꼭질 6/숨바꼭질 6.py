import sys

def gcd(a, b):
    r = 0
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

if __name__ == '__main__':
    n, s = map(int, sys.stdin.readline().split())
    brothers = list(map(int, sys.stdin.readline().split()))
    brothers.append(s)
    brothers.sort()
    gcd_ = brothers[1] - brothers[0]
    for i in range(1, len(brothers)-1):
        gcd_ = gcd(gcd_, brothers[i+1] - brothers[i])
    print(gcd_)