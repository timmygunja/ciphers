def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))


print(encrypt(88, 'hello world!'))
