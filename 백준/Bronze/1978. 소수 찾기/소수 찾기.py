# 1978
n = input()
num_list = list(map(int, input().split()))
prime_num = []
for i in num_list:
    is_prime = True
    if i < 2:
        continue
    if i == 2:
        prime_num.append(2)
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime == True:
        prime_num.append(i)
print(len(prime_num))