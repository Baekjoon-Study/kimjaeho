import sys

s = set()

def check(x):
    return x in s

def add(x):
    if not check(x):
        s.add(x)

def remove(x):
    if check(x):
        s.remove(x)

def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)

def all():
    return set([i for i in range(1, 21)])

def empty():
    return set()

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    for _ in range(m):
        command = sys.stdin.readline().split()

        if command[0] == 'add':
            add(int(command[1]))
        elif command[0] == 'remove':
            remove(int(command[1]))
        elif command[0] == 'check':
            print(int(check(int(command[1]))))
        elif command[0] == 'toggle':
            toggle(int(command[1]))
        elif command[0] == 'all':
            s = all()
        elif command[0] == 'empty':
            s = empty()
        
        # print(s)

