import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = [i for i in range(1, n+1)]

    # print(nums)
    total_len = 0
    is_odd = 1

    while len(nums) > 1:
        total_len += len(nums)
        # print(f'total_len : {total_len}, is_odd : {is_odd}')
        nums = nums[is_odd::2]
        is_odd = not(total_len % 2)
        # print(nums)
        

print(nums[0])



#                                total_len  is_odd
# 1 2 3 4 5 6 7 8 9 10 11         11         1
# 2 4 6 8 10                       16         0
# 2 6 10                                      1
# 6