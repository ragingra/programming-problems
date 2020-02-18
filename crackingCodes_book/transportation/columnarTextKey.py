import math

def getKeywordSequence(keyword):
    sequence = []
    for pos, ch in enumerate(keyword):
        previousLetters = keyword[:pos]
        newNumber = 1
        for previousPos, previousCh in enumerate(previousLetters):
            if previousCh > ch:
                sequence[previousPos] += 1
            else:
                newNumber += 1
        sequence.append(newNumber)
    return sequence

def encrypt(text, key):
    output = []
    
    for num in getKeywordSequence(key):
        output.append(text[num-1::len(key)])
    return ''.join(output)

def decrypt(text, key):
    num_columns = math.ceil(len(text) / len(key))
    blanks = (num_columns * len(key)) - len(text)
    output = [''] * num_columns

    sequence = getKeywordSequence(key)

    column = row = 0
    for symbol in text:
        output[column] += symbol
        column += 1
        if (column == num_columns or (column == num_columns - 1 and row >= len(key) - blanks)):
            column = 0
            row += 1

    output = ([''.join([column[sequence[i]-1] for i in range(len(column))]) for column in output])

    return ''.join(output)

message = "This is a secret message!"

key = "acbd"

print(f"Original: '{message}'")
encrypted = encrypt(message, key)
print(f"Encypted: '{encrypted}'")
decrypted = decrypt(encrypted, key)
print(f"Decrypted: '{decrypted}'")