word = input()
if word[0]== word[0].upper():
    print(word)
else:
    word = word[0].upper() + word[:0] + word[1:]
    print(word)