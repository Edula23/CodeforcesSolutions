letters = input()
length = len(letters)
distinct = 0
for i in letters:
    if letters.count(i) >= 1:
        distinct+=1
        letters.replace(i, '')

print(distinct)
if distinct%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM")