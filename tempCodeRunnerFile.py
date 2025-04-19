testCases= int(input())
numbers=[]
for i in range(testCases):
    numbers.append(int(input()))
maximum = max(numbers)
polycarp = []
for i in range(maximum*2):
    if i%3!=0 and i%10!=3:
        polycarp.append(i)
for i in numbers:
    print(polycarp[i-1])
