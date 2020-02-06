keyrange = range(ord('A'), ord('Z') + 1) + range(ord('a'), ord('z') + 1) + range(ord('0'), ord('9') + 1)

l2i = {chr(value):i for i, value in enumerate(keyrange)}
i2l = {i:chr(value) for i, value in enumerate(keyrange)}

def encrypt(message, key):
    output = ""
    for char in message:
        if char in l2i:
            output += i2l[(l2i[char] + key) % len(l2i)]
        else:
            output += char
    return output

def decrypt(message, key):
    output = ""
    for char in message:
        if char in l2i:
            output += i2l[(l2i[char] - key) % len(l2i)]
        else:
            output += char
    return output

encrypted = encrypt("no one will be able to read this...", 20)
print(encrypted)
decrypted = decrypt(encrypted, 20)
print(decrypted)