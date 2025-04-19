
# testCases = int(input())

# for i in range(testCases):
#    numbers = list(map(int, input().split(maxsplit = 2)))
#    if numbers[2] == numbers[0] + numbers[1]:
#        print("+")
#        continue
#    elif numbers[2] == numbers[0] - numbers[1]:
#        print("-")
#        continue
#testCases = int(input())
#codeforces  = "codeforces"

#for i in range(testCases):
#    letter = input()
#    if letter in codeforces:
#        print("YES")
#    else:
#        print("NO")
#testCases = int(input())
#for i in range(testCases):
#    number = list(map(int, input().split(maxsplit = 2)))
#    if number[0]  != number[1] and number[0] != number[2]:
#        print(number[0])
#    elif number[1]  != number[0] and number[1] != number[2]:
#       print(number[1])
#    elif number[2]  != number[0] and number[2] != number[1]:
#        print(number[2])
#testCases = int(input())
#original = ['a', 'b', 'c']
#for i in range(testCases):
#     abc = list(input())
#     if abc == original:
#        print("YES")
#     else:
#        new = abc
 #       new[0], new[1] = new[1], new[0]        
  #      if new == original:
   #         print("YES")
    #    else:
     #       new[0], new[1] = new[1], new[0] 
      #      new[0], new[2] = new[2], new[0]
       #     if new == original:
        #        print("YES")
         #   else:
          #      new[0], new[2] = new[2], new[0]
           #     new[1], new[2]= new[2], new[1]
            ##    if new == original:
              #      print("YES")
               ##    print("NO"
# testCases = int(input())   
#for i in range(testCases):
#    ticket = input()
 #   ticket_list = list(map(int, ticket))
  #  if ticket_list[0] + ticket_list[1] + ticket_list[2] == # ticket_list[3] + ticket_list[4] + ticket_list[5] :
  #      print("YES")
   # else:
    #    print("NO")

#for i in range(testCases):
    # integer = int(input())
    # if integer%10==0 or integer in range(10):
      #  print(integer)
    
    # else:
        # x=0
        # while x == 0:
         #   remainder = integer % 10
        #    integer -= remainder
       #     if integer%10 == 0:
    #            print(integer, remainder)
   #             break
  #          else:
 #               x+=1
#                continue
#testCases = int(input())
#original = ["T","i","m","u","r"]
#for i in range(testCases):
#    stringLength = int(input())
#    name = list(input())
#    included = False
#    if stringLength == 5:
 #       for char in name:
  #          if char in original:
   #             included = True
    #        else:
     #           print("NO")
      #          included = False
       #         break
        #if included:
         #   print("YES")
    #else:
     #   print("NO")            
#rating = int(input())
#if rating >= 1 and rating <= 3000:
 #   if rating < 1200:
  #      print("ABC")
   # else:
    #    print("ARC")
#colors = list(map(int, input().split(maxsplit=2)))
#if colors[0]==colors[1] and colors[1]==colors[2]:
#    numberOfcolors = 1
#elif colors[0]==colors[1] and colors[1]!=colors[2]:
 #   numberOfcolors = 2
#elif colors[1]==colors[2] and colors[1]!=colors[0]:
 #   numberOfcolors = 2
#elif colors[0]==colors[2] and colors[1]!=colors[0]:
 #   numberOfcolors = 2
#else:
 #   numberOfcolors = 3
#print(numberOfcolors)
letter = input()
vowels = ['a', 'e', 'i', 'o', 'u']
if letter in vowels:
    print("vowel")
else:
    print("consonalt")



