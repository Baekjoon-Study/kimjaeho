import sys

if __name__ == '__main__':
    l = int(sys.stdin.readline())

    string = sys.stdin.readline().rstrip()
    hash = 0

    for i in range(len(string)):
        a_i = ord(string[i]) - 96
        hash += a_i * (31 ** i)
    
    hash %= 1234567891
    print(hash)