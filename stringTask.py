text = input()
text=text.lower()
for i in text: 
    if i == "a" or i == "e" or i == "i" or  i == "u" or i == "o" or i=="y":
        text=text.replace(i, "")
text = list(text)     
for i in range((len(text))*2):    
    if i%2==0:
        text.insert(i, ".")
text = "".join(text)
print(text) 
        
