import sys

n = int(sys.stdin.readline())
for i in range(n):
    ox = sys.stdin.readline().rstrip()

    is_cumul = 0
    grading = 0
    for i in ox:
        if i == 'O':
            is_cumul += 1
            grading += is_cumul
        elif i == 'X':
            is_cumul = 0
    
    print(grading)