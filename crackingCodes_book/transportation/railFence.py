import itertools

def encrypt(text, key):
    output = [[] for num in range(key)]
    column = 0
    increase = False 

    for char in text:
        output[column].append(char)

        if column == key -1 or column == 0:
            increase = not increase

        if increase:
            column += 1
        else:
            column -= 1

    return ''.join(itertools.chain(*output))

message = "Common sense is not so common."
key = 3

print(f"Message: {message}")
encrypted = encrypt(message, key)
print(f"Encypted: {encrypted}")