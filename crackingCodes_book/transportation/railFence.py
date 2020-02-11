from itertools import cycle

def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])

def encrypt(text, key):
    p = rail_pattern(key)
    return ''.join(sorted(text, key=lambda i: next(p)))

def decrypt(text, key):
    p = rail_pattern(key)
    indexes = sorted(range(len(text)), key=lambda i: next(p))
    output = [''] * len(text)
    for i, c in zip(indexes, text):
        output[i] = c
    return ''.join(output)

message = "Common sense is not so common."
key = 3

print(f"Message: {message}")
encrypted = encrypt(message, key)
print(f"Encypted: {encrypted}")
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")