import math

def encrypt(text, key):
    output = []
    for num in range(key):
        output.append(text[num::key])
    return ''.join(output)

def decrypt(text, key):
    num_columns = math.ceil(len(text) / key)
    blanks = (num_columns * key) - len(text)
    output = [''] * num_columns

    column = row = 0
    for symbol in text:
        output[column] += symbol
        column += 1
        if (column == num_columns or (column == num_columns - 1 and row >= key - blanks)):
            column = 0
            row += 1
    return ''.join(output)

message = "Common sense is not so common."

key = 8

print(f"Original: '{message}'")
encrypted = encrypt(message, key)
print(f"Encypted: '{encrypted}'")
decrypted = decrypt(encrypted, key)
print(f"Decypted: '{decrypted}'")