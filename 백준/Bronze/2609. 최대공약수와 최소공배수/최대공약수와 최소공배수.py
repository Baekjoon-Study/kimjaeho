a, b = map(int, input().split())

def gcd(a, b):
    r = 0
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

gcd = gcd(a, b)
print(gcd)
print(a * b // gcd)