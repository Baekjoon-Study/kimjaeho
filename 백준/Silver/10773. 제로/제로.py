import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = []
    for i in range(n):
        num = int(sys.stdin.readline())
        if num:
            nums.append(num)
        else:
            nums.pop(-1)

    print(sum(nums))