import sys

fb = ['FizzBuzz', 'Fizz', 'Buzz']

def fizzbuzz(i):
    rst = ''
    if i % 3 == 0:
        rst += 'Fizz'
    if i % 5 == 0:
        rst += 'Buzz'
    return rst if len(rst) else i


if __name__ == '__main__':
    n = 0
    for i in range(3, 0, -1):
        tmp = sys.stdin.readline().rstrip()
        if tmp not in fb:
            n = int(tmp) + i
    
    print(fizzbuzz(n))
