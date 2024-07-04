import sys

iron_bars = sys.stdin.readline().rstrip()
before, iron_bars = iron_bars[0], iron_bars[1:]
stack = []
bar_cnt = 0

for i in iron_bars:
    if before == '(':
        if i == '(':
            stack.append(before)
        else: # i == ')'
            bar_cnt += len(stack)
    else: # before == ')'
        if i == ')':
            bar_cnt += 1
            stack.pop(-1)
    before = i

print(bar_cnt)

