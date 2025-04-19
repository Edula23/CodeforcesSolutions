'''course = 'Python for Beginners'
print(course.upper())
print(course)
print(course.find('Beginners'))
print(course.replace('for', '4'))
print('Python' in course)
print(10/3)
print(10//3)
print(10**3)
price = 5
print(not price>10) and or not 
if price > 2:
    print('hellow')
elif price==5:
    print('hehe')'''
'''weight = int(input('Weight: '))
measurement = input('(K)g or (L)bs: ')
if(measurement.upper()=='K'):
    print(weight*10)
elif(measurement.upper()=='L'):
    print(weight/10)
i=1
while i<=5:
    print(i*'*')
    i=i+1
name = ['eden', 'lala', 'dora', 'flicity']
print (name[-1])
print (name)
print(name[0:3])'''
numbers = [1, 2, 3, 4 ,5]
numbers.append(6)
print(numbers)
numbers.insert(0, 'Hi')
print(numbers)
# numbers.remove(3)
# numbers.clear()
print(1 in numbers)
print(len(numbers))
for item in numbers:
    print(item)
numbers2 = range(5, 10, 2)
for n in numbers2:
    print(n)

numbers3 = (1, 2, 3, 3)
print(numbers3.count(3))#.index
alphabets = ['ol', 'gkl', 'hji', 'abh', 'uif']
print (alphabets[::2])
print (alphabets[::-1])
print(dir(alphabets)) # prints methods
print(help(alphabets)) # prints purposes of the methods
alphabets.sort() # sorts in alphabetical ordrer
alphabets.reverse() #reverses a string