# 1193
x = int(input())
i = 1
j = 1
while True:
    if x - i <= 0:
        break
    x -= i
    i += 1
    j += 1
if j % 2 == 1:
    print("{}/{}".format(j - x + 1, x))
else:
    print("{}/{}".format(x, j - x + 1))