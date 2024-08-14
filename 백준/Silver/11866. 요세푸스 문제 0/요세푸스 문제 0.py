import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    idx = k
    circle = [i for i in range(1, n+1)]
    josephus = []

    # print(idx, len(circle))
    josephus.append(circle.pop(idx-1))
    while len(circle):
        idx = (idx + (k-1)) % len(circle)
        if idx == 0:
            idx = len(circle)
        # print(idx, len(circle))
        josephus.append(circle.pop(idx-1))
    print(f"<{', '.join(map(str, josephus))}>")