import sys

if __name__ == '__main__':
    repeat = int(sys.stdin.readline())
    for i in range(repeat):
        n, m = map(int, sys.stdin.readline().split())

        queue = list(map(int, sys.stdin.readline().split()))
        target = [0 for i in range(len(queue))]

        target[m] = 1
        order = 0

        # print(f'queue : {queue}')
        # print(f'target : {target}')

        while True:
            if queue[0] == max(queue):
                order += 1
                if target[0] == 1:
                    print(order)
                    break
                queue.pop(0)
                target.pop(0)
                # print(f'queue : {queue}')
                # print(f'target : {target}')
            else:
                queue.append(queue.pop(0))
                target.append(target.pop(0))
                # print(f'queue : {queue}')
                # print(f'target : {target}')