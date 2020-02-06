keyrange = range(ord('A'), ord('Z') + 1) + range(ord('a'), ord('z') + 1) + range(ord('0'), ord('9') + 1)

l2i = {chr(value):i for i, value in enumerate(keyrange)}
i2l = {i:chr(value) for i, value in enumerate(keyrange)}

message = "78 87y G255 vy uv5y D8 Byux D12C..."

def decrypt(message, key):
    output = ""
    for char in message:
        if char in l2i:
            output += i2l[(l2i[char] - key) % len(l2i)]
        else:
            output += char
    return output

for number in range(len(l2i)):
    decrypted = decrypt(message, number)
    print("Key: {}, Message: {}".format(number, decrypted))