import sys

tmp = ''
while True:
    tmp = sys.stdin.readline()[:-1]
    if tmp == '':
        break
    rst = [0] * 4
    for i in tmp:
        if 97 <= ord(i) <= 122: # 소문자
            rst[0] += 1
        elif 65 <= ord(i) <= 90: # 대문자
            rst[1] += 1
        elif 48 <= ord(i) <= 57: # 숫자
            rst[2] += 1
        else: # 공백
            rst[3] += 1
    
    print(' '.join(map(str, rst)))