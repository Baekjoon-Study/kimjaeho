rot13 = input()
rst = ''

for i in rot13:
    if i.isalpha():
        if ord(i) >= 97:
            rst += chr(ord('a') + (ord(i) - ord('a') + 13) % 26)
        else:
            rst += chr(ord('A') + (ord(i) - ord('A') + 13) % 26)
    else:
        rst += i

print(rst)