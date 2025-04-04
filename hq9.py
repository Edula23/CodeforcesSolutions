instruction = input()
found = True
for i in instruction:
    if 'H' in instruction or 'Q' in instruction or '9' in instruction: #or '+' in instruction:
        break
    else:
        found = False
if found:
    print("YES")
else:
    print("NO")