import sys

n = int(sys.stdin.readline())

def gcd(a, b):
    r = 0
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

if __name__ == '__main__':
    for i in range(n):
        nums = list(map(int, sys.stdin.readline().split()))
        m, nums = nums[0], nums[1:]
        total = 0
        for i in range(m):
            for j in range(i+1, m):
                total += gcd(nums[i], nums[j])
    
        print(total)
