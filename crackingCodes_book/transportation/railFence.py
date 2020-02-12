from itertools import cycle

def rail_pattern(key):
    values = [num for num in range(key)]
    return cycle(values + values[-2:0:-1])

def encrypt(text, key):
    pattern = rail_pattern(key)
    return ''.join(sorted(text, key=lambda i: next(pattern)))

def decrypt(text, key):
    pattern = rail_pattern(key)
    order = sorted(range(len(text)), key=lambda i: next(pattern))
    output = [''] * len(text)

    for num, char in zip(order, text):
        output[num] = char

    return ''.join(output)

message = "Common sense is not so common."
key = 3

print(f"Message: {message}")
encrypted = encrypt(message, key)
print(f"Encypted: {encrypted}")
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
