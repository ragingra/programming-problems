message = "This is a secret!"

key = 5

def encypt(text, key):
    output = ""
    for num in range(key):
        output += text[num::key]
    return output

print(message)
encrypted = encypt(message, key)
print(encrypted)