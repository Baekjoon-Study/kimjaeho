import sys

if __name__ == '__main__':
    k, n = map(int, sys.stdin.readline().split())
    lancable = [int(sys.stdin.readline()) for _ in range(k)]

    min_ = 1
    max_ = max(lancable)

    while min_ <= max_:
        mid = (min_ + max_) // 2

        lan_num = 0
        for length in lancable:
            lan_num += length // mid
        
        if lan_num < n:
            max_ = mid - 1
        else:
            min_ = mid + 1
            
    print(max_)
