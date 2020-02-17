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

    print(output)
    return ''.join(output)

message = "This is a secret message!"

key = "acbd"

print(f"Original: '{message}'")
encrypted = encrypt(message, key)
print(f"Encypted: '{encrypted}'")