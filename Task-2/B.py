word = input()

if len(word) == 1:
    word = word.upper() if word.islower() else word.lower()
elif word.isupper():
    word = word.lower()
elif word[1:].isupper():
    word = word.swapcase()

print(word)
