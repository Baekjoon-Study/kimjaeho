import sys

melody = sys.stdin.readline().rstrip()
if melody == '8 7 6 5 4 3 2 1':
    print('descending')
elif melody == '1 2 3 4 5 6 7 8':
    print('ascending')
else:
    print('mixed')