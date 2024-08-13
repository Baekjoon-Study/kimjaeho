import sys

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    A = sorted(list(map(int, sys.stdin.readline().split())))

    m = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    B = sorted(num)
    rst = {k:0 for k in num}

    i = 0
    j = 0
    while True:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            rst[B[j]] = 1
            i += 1
            j += 1

        if i == len(A) or j == len(B):
            break

    for i in num:
        print(rst[i])