# # 256 128 64 32 16 8 4 2
# # 1   1   0  0  1  1 0 0

# # 0 256  8^2 * 4
# # 1 128  8^2 * 2
# # 1 64   8^2 * 1

# # 0 32   8^1 * 4
# # 0 16   8^1 * 2
# # 1 8    8^1 * 1

# # 1 4    8^0 * 4
# # 0 2    8^0 * 2
# # 0 0    0

# import sys

# binary = sys.stdin.readline().rstrip()
# binary = '0' * (3 - len(binary)%3) + binary
# binary = list(map(int, binary))

# octa = ''
# tmp = 0
# for i in range(0, len(binary), 3):
#     tmp = 4 * binary[i] + 2 * binary[i+1] + 1 * binary[i+2]
#     octa += str(tmp)
#     # print(tmp)

# print(octa.lstrip('0'))

print(oct(int(input(), 2))[2:])