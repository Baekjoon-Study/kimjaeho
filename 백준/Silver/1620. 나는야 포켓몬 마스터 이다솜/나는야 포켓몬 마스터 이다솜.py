import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    ency = {}
    encyclopedia = [0 for _ in range(n+1)]

    for i in range(n):
        pokemon = sys.stdin.readline().rstrip()
        ency[pokemon] = i+1
        encyclopedia[i+1] = pokemon

    for _ in range(m):
        tmp = sys.stdin.readline().rstrip()
        if tmp.isalpha():
            print(ency[tmp])
        else:
            print(encyclopedia[int(tmp)])
        # if tmp in encyclopedia:
        #     print(encyclopedia[tmp])
        # else:
        #     print([k for k, v in encyclopedia.items() if v == tmp][0])